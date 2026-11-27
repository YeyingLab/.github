"""Refresh the number badges used by profile/README.md.

GitHub's image proxy often times out on shields.io, so the README does not
link to shields.io for numbers. Instead it shows SVG files stored in this repo
(profile/badges/<slug>.svg). This script looks up each number and rewrites it in
the stored SVG (a brand-new badge is rendered once on shields.io). The README
itself never changes.

The README tells the script what each badge counts:

  <a href="https://github.com/OWNER/REPO"><img src=".../profile/badges/stars-....svg">     GitHub stars
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hfdl-data-....svg">     dataset downloads (all time)
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hfdl-model-....svg">    model downloads (all time)
  <a href="https://huggingface.co/..."><img src=".../profile/badges/hflike-model-....svg">  model likes
  <a href="https://huggingface.co/papers/ID"><img src=".../profile/badges/hfpaper-ID.svg">  Hugging Face paper upvotes
  <a href="https://github.com/ORG"><img src=".../profile/badges/orgstars-ORG.svg">          total org stars
  <img src=".../profile/badges/sumhfdl-data-....svg">    all-time dataset downloads over every HF link in the README
  <img src=".../profile/badges/sumhfdl-model-....svg">   all-time model downloads over every HF link in the README
  <img src=".../profile/badges/sumhfpaper-....svg">      paper upvotes over every HF paper link in the README

If a lookup or render fails, the old SVG stays. SVGs the README no longer uses
are deleted. Run: python3 scripts/update_badges.py
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
    "hfdl-prodata": ("🤗 Pro data ⬇", "ffcc4d", "labelColor=24292f"),
    "hfdl-model": ("🤗 Model ⬇", "ffcc4d", "labelColor=24292f"),
    "hflike-model": ("🤗 Model ♥", "ffcc4d", "labelColor=24292f"),
    "orgstars": ("GitHub stars", "f5c518", "logo=github&labelColor=24292f"),
    "sumhfdl-data": ("🤗 Dataset downloads", "ffcc4d", "labelColor=24292f"),
    "sumhfdl-model": ("🤗 Model downloads", "ffcc4d", "labelColor=24292f"),
    "hfpaper": ("🤗 Paper ▲", "ffcc4d", "labelColor=24292f"),
    "sumhfpaper": ("🤗 Paper upvotes", "ffcc4d", "labelColor=24292f"),
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


def hf_repos(href):
    """(kind, repo id) pairs behind a Hugging Face link; a collection expands to its items."""
    path = urllib.parse.urlparse(href).path.strip("/").split("/")
    if path[0] == "collections":
        items = get_json(f"https://huggingface.co/api/collections/{'/'.join(path[1:3])}")["items"]
        return [(i["type"] + "s", i["id"]) for i in items if i.get("type") in ("model", "dataset", "space")]
    if path[0] in ("datasets", "spaces"):
        return [(path[0], "/".join(path[1:3]))]
    return [("models", "/".join(path[0:2]))]


def hf_value(kind, rid, field):
    data = get_json(f"https://huggingface.co/api/{kind}/{rid}?expand%5B%5D={field}")
    return int(data.get(field) or 0)


def hf_count(href, field):
    return sum(hf_value(kind, rid, field) for kind, rid in hf_repos(href))


def paper_upvotes(href):
    pid = urllib.parse.urlparse(href).path.strip("/").split("/")[1]
    return int(get_json(f"https://huggingface.co/api/papers/{pid}").get("upvotes") or 0)


def paper_total(text):
    links = set(re.findall(r'href="(https://huggingface\.co/papers/[^"/]+)"', text))
    return sum(paper_upvotes(h) for h in sorted(links))


EXTRA = os.path.join(ROOT, "scripts", "hf_repos.txt")


def hf_total(text, kind):
    """All-time downloads summed over every distinct Hugging Face repo linked in the README,
    plus the extra lab repos listed in scripts/hf_repos.txt."""
    repos = set()
    for href in set(re.findall(r'href="(https://huggingface\.co/(?!papers/)[^"]+)"', text)):
        repos.update(hf_repos(href))
    if os.path.exists(EXTRA):
        for line in open(EXTRA, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#"):
                k, rid = line.split("/", 1)
                repos.add((k, rid))
    return sum(hf_value(k, rid, "downloadsAllTime") for k, rid in sorted(repos) if k == kind)


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
    style = "social" if 'id="llink"' in svg else "flat"
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
            for m in re.finditer(r'(?:<a href="(?P<href>[^"]+)">)?<img src="' + RAW + r'(?P<slug>[a-z0-9._-]+)\.svg"', text)]
    jobs = list(dict.fromkeys(jobs))

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
                n = org_stars(urllib.parse.urlparse(target).path.strip("/").split("/")[0])
            elif kind == "sumhfdl-data":
                n = hf_total(text, "datasets")
            elif kind == "sumhfdl-model":
                n = hf_total(text, "models")
            elif kind == "hfpaper":
                n = paper_upvotes(target)
            elif kind == "sumhfpaper":
                n = paper_total(text)
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
    removed = remove_unused({slug for slug, _ in jobs})
    print(f"{len(jobs)} badges, {changed} updated, {failed} failed, {removed} unused removed")


def remove_unused(used):
    """Delete badge SVGs the README no longer shows (e.g. after a repo moved)."""
    if len(used) < 10:  # README not parsed as expected; delete nothing
        return 0
    removed = 0
    for name in sorted(os.listdir(BADGES)):
        if name.endswith(".svg") and name[:-4] not in used:
            os.remove(os.path.join(BADGES, name))
            removed += 1
            print(f"removed unused {name}")
    return removed


if __name__ == "__main__":
    main()
