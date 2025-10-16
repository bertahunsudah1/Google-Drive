#!/usr/bin/env python3
"""
Example CLI: simple header utils - non-destructive
"""
import argparse, sys, json
from urllib.request import Request, urlopen

def fetch_headers(url, timeout=6):
    headers = {"User-Agent": "DarkGithub-Example/0.4"}
    req = Request(url, headers=headers, method="GET")
    with urlopen(req, timeout=timeout) as r:
        return dict(r.getheaders()), r.getcode(), r.geturl()

def cli():
    p = argparse.ArgumentParser(prog="main.py")
    p.add_argument("url", help="URL to fetch headers for")
    p.add_argument("--json", action="store_true", help="output JSON")
    args = p.parse_args()
    try:
        hdrs, code, final = fetch_headers(args.url)
    except Exception as e:
        print("error:", e, file=sys.stderr)
        return 2
    out = {"url": final, "status": code, "headers": hdrs}
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print("URL:", final)
        print("Status:", code)
        for k,v in hdrs.items():
            print(f"{k}: {v}")
    return 0

if __name__ == "__main__":
    sys.exit(cli())
