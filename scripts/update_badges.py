"""Refresh the number badges used by profile/README.md.

GitHub's image proxy often times out on shields.io, so the README does not
link to shields.io for numbers. Instead it shows SVG files stored in this repo
(profile/badges/<slug>.svg). This script looks up each number, renders the badge
once through shields.io, and saves the SVG. The README itself never changes.

The README tells the script what each badge counts:

  <a href="https://github.com/OWNER/REPO"><img src=".../profile/badges/stars-....svg">     GitHub stars
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hfdl-data-....svg">     dataset downloads (all time)
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hfdl-model-....svg">    model downloads (all time)
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hflike-model-....svg">  model likes
  [![Total stars](.../profile/badges/orgstars-ORG.svg)](https://github.com/ORG)             total org stars

If a lookup or render fails, the old SVG stays. Run: python3 scripts/update_badges.py
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
README = os.path.join(ROOT, "profile", "README.md")
BADGES = os.path.join(ROOT, "profile", "badges")
TOKEN = os.environ.get("GITHUB_TOKEN")
RAW = r"https://raw\.githubusercontent\.com/YeyingLab/\.github/main/profile/badges/"

STYLES = {
    "stars": ("Code ★", "f5c518", "logo=github&labelColor=24292f"),
    "hfdl-data": ("🤗 Data ⬇", "ffcc4d", "labelColor=24292f"),
    "hfdl-model": ("🤗 Model ⬇", "ffcc4d", "labelColor=24292f"),
    "hflike-model": ("🤗 Model ♥", "ffcc4d", "labelColor=24292f"),
    "orgstars": ("Stars", "blue", "style=social&logo=github"),
}


def fetch(url, accept="application/json"):
    headers = {"User-Agent": "yeyinglab-badge-updater", "Accept": accept}
    if TOKEN and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return r.read()


def get_json(url):
    return json.loads(fetch(url))


def github_stars(href):
    repo = "/".join(urllib.parse.urlparse(href).path.strip("/").split("/")[:2])
    return int(get_json(f"https://api.github.com/repos/{repo}")["stargazers_count"])


def org_stars(org):
    total, page = 0, 1
    while True:
        repos = get_json(f"https://api.github.com/orgs/{org}/repos?type=public&per_page=100&page={page}")
        total += sum(int(r["stargazers_count"]) for r in repos)
        if len(repos) < 100:
            return total
        page += 1


def hf_count(href, field):
    path = urllib.parse.urlparse(href).path.strip("/").split("/")
    if path[0] in ("datasets", "spaces"):
        kind, rid = path[0], "/".join(path[1:3])
    else:
        kind, rid = "models", "/".join(path[0:2])
    data = get_json(f"https://huggingface.co/api/{kind}/{rid}?expand%5B%5D={field}")
    return int(data.get(field) or 0)


def render_shields(kind, number):
    """Render a badge on shields.io (used only when no SVG exists yet)."""
    label, color, query = STYLES[kind]
    enc = lambda t: urllib.parse.quote(t.replace("-", "--").replace("_", "__"), safe="")
    url = f"https://img.shields.io/badge/{enc(label)}-{enc(f'{number:,}')}-{color}?{query}"
    svg = fetch(url, accept="image/svg+xml")
    if not svg.lstrip().startswith(b"<svg"):
        raise ValueError(f"not an SVG: {url}")
    return svg


# Glyph widths (px at 11px) that shields.io uses for numbers. The flat style
# uses Verdana, the social style Helvetica bold.
WIDTHS = {
    "flat": {"digit": 6.9970703125, ",": 3.6376953125},
    "social": {"digit": 6.1162109375, ",": 3.0576171875},
}


def text_length(msg, style):
    w = sum(WIDTHS[style]["digit"] if c.isdigit() else WIDTHS[style][c] for c in msg)
    w = int(w)  # shields floors the width, then makes it odd
    return w if w % 2 else w + 1


def sub_once(pattern, repl, s):
    s2, n = re.subn(pattern, repl, s, count=1)
    if n != 1:
        raise ValueError(f"badge template mismatch: {pattern}")
    return s2


def render_local(svg, kind, number):
    """Rewrite the number in an existing shields.io SVG, keeping its exact layout."""
    svg = svg.decode("utf-8")
    label = STYLES[kind][0]
    old = re.search(r'aria-label="' + re.escape(label) + r': ([^"]+)"', svg).group(1)
    new = f"{number:,}"
    style = "social" if kind == "orgstars" else "flat"
    px = text_length(new, style)
    tl = px * 10  # SVG text is drawn at scale(.1)
    if style == "flat":
        lw = int(re.search(r'<rect width="(\d+)" height="20" fill="#', svg).group(1))
        mw = px + 10
        w = lw + mw
        mx = lw * 10 + mw * 5 - 10
        svg = sub_once(r'(<svg [^>]*?width=")\d+(")', rf"\g<1>{w}\g<2>", svg)
        svg = sub_once(r'(<clipPath id="r"><rect width=")\d+(")', rf"\g<1>{w}\g<2>", svg)
        svg = sub_once(r'(<rect x="' + str(lw) + r'" width=")\d+(")', rf"\g<1>{mw}\g<2>", svg)
        svg = sub_once(r'(<rect width=")\d+(" height="20" fill="url\(#s\)"/>)', rf"\g<1>{w}\g<2>", svg)
    else:
        bw = px + 8
        w = 61 + bw
        mx = int((60.5 + bw / 2) * 10 - 5)
        svg = sub_once(r'(<svg [^>]*?width=")\d+(")', rf"\g<1>{w}\g<2>", svg)
        svg = sub_once(r'(<rect x="60\.5" y="\.5" width=")\d+(")', rf"\g<1>{bw}\g<2>", svg)
    svg = svg.replace(f'aria-label="{label}: {old}"', f'aria-label="{label}: {new}"')
    svg = svg.replace(f"<title>{label}: {old}</title>", f"<title>{label}: {new}</title>")
    svg, n = re.subn(r'x="\d+"([^>]*?)textLength="\d+"([^>]*)>' + re.escape(old) + "<",
                     lambda m: f'x="{mx}"{m.group(1)}textLength="{tl}"{m.group(2)}>{new}<', svg)
    if n == 0:
        raise ValueError("number text not found in badge")
    return svg.encode("utf-8")


def render(kind, number, existing):
    return render_local(existing, kind, number) if existing else render_shields(kind, number)


def kind_of(slug):
    for k in sorted(STYLES, key=len, reverse=True):
        if slug.startswith(k + "-"):
            return k
    raise ValueError(f"unknown badge kind in slug {slug!r}")


def main():
    text = open(README, encoding="utf-8").read()
    jobs = [(m.group("slug"), m.group("href"))
            for m in re.finditer(r'<a href="(?P<href>[^"]+)"><img src="' + RAW + r'(?P<slug>[a-z0-9._-]+)\.svg"', text)]
    jobs += [(m.group("slug"), m.group("org"))
             for m in re.finditer(r'\[!\[Total stars\]\(' + RAW + r'(?P<slug>[a-z0-9._-]+)\.svg\)\]\(https://github\.com/(?P<org>[^/)]+)\)', text)]

    os.makedirs(BADGES, exist_ok=True)
    changed, failed = 0, 0
    for slug, target in jobs:
        kind = kind_of(slug)
        path = os.path.join(BADGES, slug + ".svg")
        old = open(path, "rb").read() if os.path.exists(path) else None
        try:
            if kind == "stars":
                n = github_stars(target)
            elif kind == "orgstars":
                n = org_stars(target)
            else:
                n = hf_count(target, "likes" if kind.startswith("hflike") else "downloadsAllTime")
            svg = render(kind, n, old)
        except Exception as e:  # keep the old SVG
            failed += 1
            print(f"FAILED  {slug}: {e}", file=sys.stderr)
            continue
        if svg != old:
            open(path, "wb").write(svg)
            changed += 1
            print(f"updated {slug}: {n:,}")
    print(f"{len(jobs)} badges, {changed} updated, {failed} failed")


if __name__ == "__main__":
    main()
