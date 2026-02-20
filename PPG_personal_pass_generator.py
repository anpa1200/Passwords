#!/usr/bin/env python3
"""
Personal Pass Generator (PPG) - Generate personalized password wordlists for security testing.

For use only in authorized penetration testing and security assessments.
Copyright (C) Andrey Pautov - 1200km@gmail.com
Licensed under GPL-3.0-or-later.
"""

import argparse
import itertools
import string
import sys
from pathlib import Path

# Predefined list of special symbols
BASIC_SPECIAL_SYMBOLS = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
    "[",
    "]",
    "{",
    "}",
    "~",
]

BANNER = """
╔═════════════════════════════════════════════════════════════════════════════╗
║                        PERSONAL PASS GENERATOR (PPG)                       ║
║                        Created by Andrey Pautov                            ║
║                         Email: 1200km@gmail.com                            ║
║─────────────────────────────────────────────────────────────────────────────║
║  ⚠  This tool may generate very large wordlists (1MB to 4TB+).             ║
║  Use for authorized security testing only. Limit to 2–5 entries for        ║
║  manageable resource usage.                                                 ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""


def _leet_speak_map() -> dict:
    return {
        "a": "@",
        "b": "8",
        "c": "(",
        "e": "3",
        "g": "9",
        "h": "#",
        "i": "!",
        "o": "0",
        "s": "$",
        "t": "7",
        "z": "2",
        "A": "4",
        "B": "8",
        "C": "(",
        "E": "3",
        "G": "9",
        "O": "0",
        "S": "$",
        "Z": "2",
    }


def to_leet_speak(values: list[str]) -> list[str]:
    """Append 1337-style variants for each value. Modifies list in place and returns it."""
    leet = _leet_speak_map()
    extra = []
    for value in values:
        new_value = "".join(leet.get(c, c) for c in value)
        if new_value != value:
            extra.append(new_value)
    values.extend(extra)
    return values


def generate_additional_values() -> list[str]:
    """Build character pool and 1/2/3-char combinations for suffix/prefix variations."""
    char_pool = (
        list(string.digits)
        + list(string.ascii_lowercase)
        + list(string.ascii_uppercase)
        + BASIC_SPECIAL_SYMBOLS
    )
    additional = list(char_pool)
    for r in (2, 3):
        for comb in itertools.product(char_pool, repeat=r):
            additional.append("".join(comb))
    return additional


def _add_variants(value: str, target: list[str]) -> None:
    if not value:
        return
    target.append(value.lower())
    target.append(value.capitalize())
    target.append(value.upper())


def _get_optional(prompt: str) -> str:
    return input(prompt).strip().lower()


def _get_birthdate(prompt: str) -> str:
    while True:
        val = input(prompt).strip().lower()
        if not val:
            return ""
        if len(val) == 8 and val.isdigit():
            return val
        print("Invalid format. Use DDMMYYYY or leave empty.")


def _get_int(prompt: str, default: int) -> int:
    while True:
        val = input(prompt).strip()
        if not val:
            return default
        try:
            n = int(val)
            if n < 0:
                raise ValueError("Must be non-negative.")
            return n
        except ValueError as e:
            print(f"Invalid input: {e}")


def gather_information_interactive() -> list[str]:
    """Collect user data interactively and return a list of basic string values."""
    basic_values = []

    user_info = {
        "first_name": _get_optional("Enter First Name (optional): "),
        "last_name": _get_optional("Enter Last Name (optional): "),
        "birthdate": _get_birthdate("Enter Birthdate (DDMMYYYY, optional): "),
        "nickname": _get_optional("Enter Nickname (optional): "),
        "phone_number": _get_optional("Enter Phone Number (optional): "),
        "ID_number": _get_optional("Enter ID Number (optional): "),
        "partners_name": _get_optional("Enter Partner's Name (optional): "),
        "partners_nickname": _get_optional("Enter Partner's Nickname (optional): "),
        "partners_birthdate": _get_birthdate("Enter Partner's Birthdate (DDMMYYYY, optional): "),
    }

    for key in (
        "first_name",
        "last_name",
        "nickname",
        "phone_number",
        "ID_number",
        "partners_name",
        "partners_nickname",
    ):
        _add_variants(user_info[key], basic_values)

    for key in ("birthdate", "partners_birthdate"):
        b = user_info[key]
        if b:
            basic_values.append(b)
            basic_values.append(b[4:])  # YYYY
            basic_values.append(b[:4])  # DDMM

    num_children = _get_int("Enter Number of Children (default 0): ", 0)
    for i in range(num_children):
        _add_variants(_get_optional(f"Enter Child {i + 1} Name (optional): "), basic_values)
        b = _get_birthdate(f"Enter Child {i + 1} Birthdate (DDMMYYYY, optional): ")
        if b:
            basic_values.append(b)
            basic_values.append(b[4:])
            basic_values.append(b[:4])

    num_pets = _get_int("Enter Number of Pets (default 0): ", 0)
    for i in range(num_pets):
        _add_variants(_get_optional(f"Enter Pet {i + 1} Name (optional): "), basic_values)

    _add_variants(_get_optional("Enter Company Name (optional): "), basic_values)
    _add_variants(_get_optional("Enter Profession (optional): "), basic_values)
    _add_variants(_get_optional("Enter Special Words (optional): "), basic_values)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for v in basic_values:
        if v and v not in seen:
            seen.add(v)
            unique.append(v)
    return unique


def generate_passwords(
    basic_values: list[str],
    additional_values: list[str],
    add_symbols: bool,
    min_len: int,
    max_len: int,
) -> set[str]:
    """Generate password set from basic and additional value lists."""
    passwords = set()

    for bval in basic_values:
        if bval:
            passwords.add(bval)

    if add_symbols:
        for bval in basic_values:
            if not bval:
                continue
            for addval in additional_values:
                passwords.add(f"{addval}{bval}")
                passwords.add(f"{bval}{addval}")
                passwords.add(f"{addval}{bval}{addval}")

        if len(basic_values) > 3:
            for bval1 in basic_values:
                for bval2 in basic_values:
                    if bval1 != bval2 and bval1 and bval2:
                        passwords.add(f"{bval1}{bval2}")
                        for addval in additional_values:
                            passwords.add(f"{addval}{bval1}{bval2}")
                            passwords.add(f"{addval}{bval1}{bval2}{addval}")
                            passwords.add(f"{bval1}{bval2}{addval}")
                            passwords.add(f"{addval}{bval1}{addval}{bval2}{addval}")
                            passwords.add(f"{bval1}{addval}{bval2}{addval}")
                            passwords.add(f"{bval1}{addval}{bval2}")
                            passwords.add(f"{addval}{bval1}{addval}{bval2}")
    else:
        if len(basic_values) > 3:
            for bval1 in basic_values:
                for bval2 in basic_values:
                    if bval1 != bval2 and bval1 and bval2:
                        passwords.add(f"{bval1}{bval2}")

    return {pw for pw in passwords if min_len <= len(pw) <= max_len}


def run_interactive(output_path: Path, min_len: int, max_len: int) -> None:
    """Interactive flow: banner, options, gather info, generate, save."""
    print(BANNER)

    mode1337 = input("Enable 1337 (leet) mode? [y/N]: ").strip().lower() or "n"
    while mode1337 not in ("y", "n"):
        mode1337 = input("Enter 'y' or 'n': ").strip().lower()

    basic_values = gather_information_interactive()
    if not basic_values:
        print("No input data. Add at least one name, date, or word.")
        sys.exit(1)

    if mode1337 == "y":
        to_leet_speak(basic_values)

    add_symbols = input("Add symbols (e.g. @pass#)? [y/N]: ").strip().lower() or "n"
    while add_symbols not in ("y", "n"):
        add_symbols = input("Enter 'y' or 'n': ").strip().lower()

    print("Generating... (this may take a few minutes)")
    additional_values = generate_additional_values()
    passwords = generate_passwords(
        basic_values,
        additional_values,
        add_symbols=(add_symbols == "y"),
        min_len=min_len,
        max_len=max_len,
    )

    with output_path.open("w", encoding="utf-8") as f:
        for pw in sorted(passwords):
            f.write(pw + "\n")

    print(f"Saved {len(passwords)} passwords to {output_path}")
    print("Generated with PPG - Personal Pass Generator | 1200km@gmail.com")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Personal Pass Generator (PPG) - personalized wordlists for security testing.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("special_list.txt"),
        help="Output wordlist file path",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=4,
        metavar="N",
        help="Minimum password length (1–20)",
    )
    parser.add_argument(
        "--max-length",
        type=int,
        default=12,
        metavar="N",
        help="Maximum password length (1–20)",
    )
    parser.add_argument(
        "--no-interactive",
        action="store_true",
        help="Skip interactive run; only validate and show defaults (use with interactive run for generation)",
    )
    args = parser.parse_args()

    min_len = max(1, min(20, args.min_length))
    max_len = max(1, min(20, args.max_length))
    if max_len < min_len:
        max_len = min_len

    if args.no_interactive:
        print("Min length:", min_len, "Max length:", max_len, "Output:", args.output)
        print("Run without --no-interactive to generate wordlists.")
        return

    run_interactive(args.output, min_len, max_len)


if __name__ == "__main__":
    main()
