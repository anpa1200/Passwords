#!/usr/bin/env python3
"""
Israeli phone number list generator for security/testing use.

Generates numbers for common Israeli mobile/VoIP/landline prefixes.
For authorized use only.
"""

import argparse
import sys
from pathlib import Path

# Common Israeli mobile, VoIP, and landline prefixes
DEFAULT_PREFIXES = ["050", "052", "053", "054", "055", "058", "072", "076", "077"]


def generate_phone_numbers(
    output_path: Path,
    prefixes: list[str] | None = None,
    digits_after_prefix: int = 7,
    limit: int | None = None,
    verbose: bool = True,
) -> int:
    """
    Write one number per line: prefix + zero-padded number.
    Returns total count written.
    """
    prefixes = prefixes or DEFAULT_PREFIXES
    total = 0
    per_prefix = 10**digits_after_prefix

    with output_path.open("w", encoding="utf-8") as f:
        for prefix in prefixes:
            for i in range(per_prefix):
                if limit is not None and total >= limit:
                    return total
                num = f"{prefix}{str(i).zfill(digits_after_prefix)}"
                f.write(num + "\n")
                total += 1
                if verbose and total % 1_000_000 == 0 and total > 0:
                    print(f"  Written {total} numbers...", file=sys.stderr)

    return total


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate Israeli phone number lists (prefix + 7 digits) for testing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("israeli_phone_numbers.txt"),
        help="Output file path",
    )
    parser.add_argument(
        "-p",
        "--prefixes",
        nargs="+",
        default=DEFAULT_PREFIXES,
        help="Prefixes to use (e.g. 050 052)",
    )
    parser.add_argument(
        "-d",
        "--digits",
        type=int,
        default=7,
        metavar="N",
        help="Digits after prefix (e.g. 7 => 0000000–9999999)",
    )
    parser.add_argument(
        "-n",
        "--limit",
        type=int,
        default=None,
        metavar="N",
        help="Stop after N numbers (useful for testing)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Do not print progress to stderr",
    )
    args = parser.parse_args()

    if args.digits < 1 or args.digits > 10:
        print("--digits must be between 1 and 10.", file=sys.stderr)
        sys.exit(1)

    count = generate_phone_numbers(
        args.output,
        prefixes=args.prefixes,
        digits_after_prefix=args.digits,
        limit=args.limit,
        verbose=not args.quiet,
    )
    if not args.quiet:
        print(f"Wrote {count} numbers to {args.output}", file=sys.stderr)


if __name__ == "__main__":
    main()
