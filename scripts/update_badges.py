"""Refresh the numbers in the static badges of profile/README.md.

Static badges always render, unlike live shields.io badges, which GitHub's
image proxy drops when shields.io is slow. This script reads each badge's
link to decide what to count, then rewrites only the number:

  <a href="https://github.com/OWNER/REPO"><img src=".../badge/Code ★-N-...">  -> GitHub stars
  <a href="https://huggingface.co/...">  label with ⬇ -> all-time downloads
  <a href="https://huggingface.co/...">  label with ♥ -> likes
  [![Total stars](.../badge/Stars-N-...)](https://github.com/ORG)          -> org total stars

If a lookup fails, the old number stays. Run: python3 scripts/update_badges.py
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request

README = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "profile", "README.md")
TOKEN = os.environ.get("GITHUB_TOKEN")


def get_json(url):
    headers = {"User-Agent": "yeyinglab-badge-updater", "Accept": "application/json"}
    if TOKEN and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as r:
        return json.load(r)


def github_stars(repo):
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
    if path[0] == "datasets":
        kind, rid = "datasets", "/".join(path[1:3])
    elif path[0] == "spaces":
        kind, rid = "spaces", "/".join(path[1:3])
    else:
        kind, rid = "models", "/".join(path[0:2])
    data = get_json(f"https://huggingface.co/api/{kind}/{rid}?expand%5B%5D={field}")
    return int(data.get(field) or 0)


def fmt(n):
    return f"{n:,}"


BADGE = re.compile(
    r'(<a href="(?P<href>[^"]+)"><img src="https://img\.shields\.io/badge/'
    r'(?P<label>(?:[^"?-]|--)+)-)(?P<msg>[0-9%C,.k]+)(?P<rest>-[0-9a-fA-F]{6}[^"]*")'
)
TOTAL = re.compile(
    r'(\[!\[Total stars\]\(https://img\.shields\.io/badge/Stars-)(?P<msg>[0-9%C,.k]+)'
    r'(?P<rest>-[^)]*\)\]\(https://github\.com/(?P<org>[^/)]+)\))'
)


def main():
    text = open(README, encoding="utf-8").read()
    changed, failed = [], []

    def update(m):
        href = m.group("href")
        label = urllib.parse.unquote(m.group("label").replace("--", "-"))
        old = urllib.parse.unquote(m.group("msg"))
        try:
            if href.startswith("https://github.com/"):
                n = github_stars("/".join(urllib.parse.urlparse(href).path.strip("/").split("/")[:2]))
            elif href.startswith("https://huggingface.co/"):
                n = hf_count(href, "likes" if "♥" in label else "downloadsAllTime")
            else:
                return m.group(0)
        except Exception as e:  # keep the old number
            failed.append(f"{href}: {e}")
            return m.group(0)
        new = fmt(n)
        if new != old:
            changed.append(f"{href} [{label}]: {old} -> {new}")
        return m.group(1) + urllib.parse.quote(new, safe="") + m.group("rest")

    text = BADGE.sub(update, text)

    def update_total(m):
        old = urllib.parse.unquote(m.group("msg"))
        try:
            new = fmt(org_stars(m.group("org")))
        except Exception as e:
            failed.append(f"org {m.group('org')}: {e}")
            return m.group(0)
        if new != old:
            changed.append(f"total stars: {old} -> {new}")
        return m.group(1) + urllib.parse.quote(new, safe="") + m.group("rest")

    text = TOTAL.sub(update_total, text)

    for line in changed:
        print("changed", line)
    for line in failed:
        print("FAILED ", line, file=sys.stderr)
    if changed:
        open(README, "w", encoding="utf-8").write(text)
    print(f"{len(changed)} badge(s) changed, {len(failed)} lookup(s) failed")


if __name__ == "__main__":
    main()
