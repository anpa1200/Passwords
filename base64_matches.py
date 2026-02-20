#!/usr/bin/env python3
"""
Base64-encode username:password pairs for HTTP Basic Auth / credential testing.

Reads usernames and passwords from files or stdin, outputs base64 lines.
For authorized security testing only.
"""

import argparse
import base64
import sys
from pathlib import Path


def encode_basic_auth(username: str, password: str) -> str:
    """Return base64-encoded 'username:password' for HTTP Basic Auth."""
    combined = f"{username}:{password}"
    return base64.b64encode(combined.encode("utf-8")).decode("utf-8")


def read_lines(path: Path) -> list[str]:
    """Read file and return non-empty stripped lines. Raises on error."""
    with path.open("r", encoding="utf-8", errors="replace") as f:
        return [line.strip() for line in f if line.strip()]


def process_pairs(usernames: list[str], passwords: list[str]) -> list[str]:
    """Cartesian product: each username with each password, base64-encoded."""
    return [
        encode_basic_auth(u, p)
        for u in usernames
        for p in passwords
    ]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate base64 username:password pairs for Basic Auth / credential testing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-u",
        "--usernames",
        type=Path,
        default=None,
        metavar="FILE",
        help="File with one username per line (or use single -U)",
    )
    parser.add_argument(
        "-U",
        "--username",
        type=str,
        default=None,
        metavar="USER",
        help="Single username (overrides --usernames if set)",
    )
    parser.add_argument(
        "-p",
        "--passwords",
        type=Path,
        default=None,
        metavar="FILE",
        help="File with one password per line (required in CLI mode)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("matches_base64.txt"),
        help="Output file path",
    )
    args = parser.parse_args()

    # Interactive mode when passwords file not given
    if args.passwords is None:
        args.passwords = Path(input("Path to passwords file: ").strip())
        if not args.passwords.is_file():
            print(f"Error: File not found: {args.passwords}", file=sys.stderr)
            sys.exit(1)
        response = input("Single username? (y/n): ").strip().lower()
        while response not in ("y", "n"):
            response = input("Enter 'y' or 'n': ").strip().lower()
        if response == "y":
            args.username = input("Username: ").strip() or "user"
            args.usernames = None
        else:
            path = input("Path to usernames file: ").strip()
            args.usernames = Path(path) if path else None
            args.username = None

    if args.passwords is not None and not args.passwords.is_file():
        print(f"Error: Passwords file not found: {args.passwords}", file=sys.stderr)
        sys.exit(1)

    if args.passwords is None:
        print("Error: Passwords file is required.", file=sys.stderr)
        sys.exit(1)

    passwords = read_lines(args.passwords)
    if not passwords:
        print("Error: No passwords found in file.", file=sys.stderr)
        sys.exit(1)

    if args.username is not None:
        usernames = [args.username]
    elif args.usernames is not None:
        if not args.usernames.is_file():
            print(f"Error: Usernames file not found: {args.usernames}", file=sys.stderr)
            sys.exit(1)
        usernames = read_lines(args.usernames)
        if not usernames:
            print("Error: No usernames found in file.", file=sys.stderr)
            sys.exit(1)
    else:
        # CLI mode but neither -U nor -u given
        print("Error: Provide --username or --usernames when using --passwords.", file=sys.stderr)
        sys.exit(1)

    encoded = process_pairs(usernames, passwords)
    with args.output.open("w", encoding="utf-8") as f:
        for line in encoded:
            f.write(line + "\n")
    print(f"Wrote {len(encoded)} encoded pairs to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
