# Passwords Toolkit

Security testing toolkit for generating wordlists, phone number lists, and Base64-encoded credentials. Intended for **authorized penetration testing and security assessments only**.

---

## Overview

| Script | Language | Purpose |
|--------|----------|---------|
| **PPG_personal_pass_generator.py** | Python | Personalized password wordlists from names, dates, 1337, symbols |
| **phone_numbers_gen.py** | Python | Israeli phone number lists (configurable prefixes/length) |
| **base64_matches.py** | Python | Base64 `username:password` pairs for HTTP Basic Auth testing |
| **generate_phone_numbers.cpp** | C++ | Same as phone generator, optimized for full 90M-number runs |

**Requirements:** Python 3.9+ for Python tools; C++17 compiler (g++, clang++) for the C++ generator.

---

## Installation

```bash
git clone https://github.com/anpa1200/Passwords.git
cd Passwords
pip install -e .
# Optional: tests and linting
pip install -e ".[dev]"
```

---

## Script 1: PPG – Personal Pass Generator

**File:** `PPG_personal_pass_generator.py`

### What it does

PPG builds **personalized password wordlists** for credential stuffing, brute-force, or dictionary attacks in authorized pentests. It takes information about a person (names, birthdates, nicknames, family, pets, company, etc.) and generates a large set of candidate passwords by:

- Using each value in **lowercase**, **Capitalized**, and **UPPERCASE**
- Optionally applying **1337 (leet) substitutions** (e.g. `a`→`@`, `e`→`3`, `s`→`$`)
- Optionally **combining** base values with a character pool: single chars, two-char and three-char combinations of digits, letters, and symbols (e.g. `@pass`, `pass123`, `!john!`)
- Combining multiple base values (e.g. first name + birth year)
- **Filtering** by minimum and maximum password length

So instead of a generic wordlist, you get a list tailored to a specific target (e.g. “John”, “1990”, “football”) that matches how people often choose passwords.

### When to use it

- Red-team or pentest where you have OSINT on a person (name, DOB, hobbies, company)
- Testing password policies with “realistic” weak passwords
- Training or workshops on password strength

### How to run

**Interactive (prompts for all data and options):**

```bash
python PPG_personal_pass_generator.py
```

You will be asked: 1337 mode (y/n), first/last name, birthdate (DDMMYYYY), nickname, phone, ID, partner/children/pets, company, profession, “special words”, whether to add symbols, and min/max length. Output is written to a text file, one password per line.

**With CLI options (output path and length; data still entered interactively):**

```bash
python PPG_personal_pass_generator.py -o my_list.txt --min-length 6 --max-length 14
```

**Options**

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output file path (default: `special_list.txt`) |
| `--min-length` | Minimum password length, 1–20 (default: 4) |
| `--max-length` | Maximum password length, 1–20 (default: 12) |
| `--no-interactive` | Only print defaults and exit; no generation |

### Output

A text file with one candidate password per line, sorted and deduplicated. Size depends heavily on how many fields you fill and whether you enable symbols and 1337.

### Resource warning

With **all** fields filled and “add symbols” enabled, PPG can produce **very large** wordlists (hundreds of MB to many GB, and in extreme cases up to TB scale) and use a lot of CPU and RAM. **Recommendation:** use **2–5** high-value entries (e.g. first name, birth year, nickname) and sensible `--min-length` / `--max-length` to keep runs manageable.

---

## Script 2: Phone number generator (Python)

**File:** `phone_numbers_gen.py`

### What it does

Generates a **list of phone numbers** by iterating over one or more **prefixes** and a **fixed number of digits** after each prefix. Each line is one number (e.g. `0501234567`). Default prefixes are Israeli mobile/VoIP/landline (050, 052, 053, 054, 055, 058, 072, 076, 077) with **7 digits** after the prefix, i.e. 9 prefixes × 10^7 = **90 million** numbers if you don’t limit.

Typical uses: SMS/voice testing, toll fraud checks, or any scenario where you need a full or partial number space in a given region/prefix.

### When to use it

- Generating input lists for tools that test phone-based auth or rate limiting
- Building region-specific number lists for Israeli numbers
- Quick samples with `--limit` for testing pipelines

### How to run

**Full default list (90M numbers, can be slow and large file):**

```bash
python phone_numbers_gen.py -o israeli_phone_numbers.txt
```

**One prefix, limited count (e.g. 10k lines for testing):**

```bash
python phone_numbers_gen.py -p 050 -o 050_sample.txt -n 10000
```

**Custom prefixes, quiet (no progress to stderr):**

```bash
python phone_numbers_gen.py --prefixes 050 052 054 -o mobile.txt -q
```

**Options**

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output file (default: `israeli_phone_numbers.txt`) |
| `-p`, `--prefixes` | One or more prefixes, space-separated (default: Israeli set) |
| `-d`, `--digits` | Number of digits after prefix, 1–10 (default: 7) |
| `-n`, `--limit` | Stop after this many numbers (optional; useful for tests) |
| `-q`, `--quiet` | No progress messages to stderr |

### Output

Plain text file, one number per line (e.g. `0500000000` … `0509999999`). With default settings and no `--limit`, the file is very large (~900 MB+ for 90M lines).

---

## Script 3: Base64 credential pairs

**File:** `base64_matches.py`

### What it does

Takes **usernames** and **passwords** (either one username or a list, and a list of passwords) and outputs the **Base64 encoding** of `username:password` for each pair, one per line. That’s exactly the format used in HTTP **Basic Authentication** (`Authorization: Basic <base64>`). Many tools (e.g. for brute-forcing or credential stuffing) expect a list of such precomputed Base64 strings so they can try them without encoding on the fly.

So: you provide a username (or file of usernames) and a file of passwords; the script produces every combination as Base64 and writes them to a file.

### When to use it

- Preparing input for tools that test HTTP Basic Auth endpoints
- Building “username:password” credential lists in the form expected by scanners or custom scripts
- Reducing repeated encoding when you have fixed username/password lists

### How to run

**Single username + password file (CLI):**

```bash
python base64_matches.py -U admin -p passwords.txt -o matches_base64.txt
```

**Username list × password list (Cartesian product):**

```bash
python base64_matches.py -u usernames.txt -p passwords.txt -o matches_base64.txt
```

**Interactive (no arguments; script will ask for file paths and single vs multiple username):**

```bash
python base64_matches.py
```

**Options**

| Option | Description |
|--------|-------------|
| `-U`, `--username` | Single username (overrides `--usernames` if both given) |
| `-u`, `--usernames` | File with one username per line |
| `-p`, `--passwords` | File with one password per line (required in CLI mode) |
| `-o`, `--output` | Output file (default: `matches_base64.txt`) |

### Output

One Base64 string per line. Each line is `base64(username + ":" + password)`. Decoding a line gives back `username:password`. Number of lines = (number of usernames) × (number of passwords).

---

## Script 4: Phone number generator (C++)

**File:** `generate_phone_numbers.cpp`

### What it does

Same idea as **phone_numbers_gen.py**: generates all numbers for a fixed set of **prefixes** with a fixed **number of digits** after the prefix. The C++ version uses the same default Israeli prefixes and 7 digits (90 million numbers total). It has no limit option and no configurable prefixes from the command line—those are fixed in the source. The benefit is **speed and low memory**: writing tens of millions of lines is faster in C++ than in Python, so for “full” runs this is the preferred option.

### When to use it

- You need the **full** Israeli default number list (all 9 prefixes × 10^7) and want the fastest run.
- You’re fine editing the source to change prefixes or digit count.

### Build

```bash
make cpp
# or
g++ -Wall -Wextra -std=c++17 -O2 -o generate_phone_numbers generate_phone_numbers.cpp
```

### How to run

**Default output file `israeli_phone_numbers.txt`:**

```bash
./generate_phone_numbers
```

**Custom output path:**

```bash
./generate_phone_numbers /path/to/out.txt
```

### Output

Same as the Python script: one number per line (prefix + zero-padded digits). With defaults, 90M lines. To change prefixes or digit count, edit the `kPrefixes` and `kDigitsAfterPrefix` / `kMaxNumber` constants in the source and recompile.

---

## Quick reference

| Task | Command |
|------|--------|
| PPG interactive | `python PPG_personal_pass_generator.py` |
| PPG with length/output | `python PPG_personal_pass_generator.py -o out.txt --min-length 6 --max-length 14` |
| Phone list (Python, sample) | `python phone_numbers_gen.py -p 050 -n 10000 -o 050.txt` |
| Phone list (Python, full) | `python phone_numbers_gen.py -o israeli_phone_numbers.txt` |
| Base64 one user | `python base64_matches.py -U admin -p pass.txt -o b64.txt` |
| Base64 user list × pass list | `python base64_matches.py -u users.txt -p pass.txt -o b64.txt` |
| Phone list (C++) | `make cpp && ./generate_phone_numbers [out.txt]` |

---

## Tests

```bash
python3 -m pytest tests/ -v
```

---

## License and author

- **Author:** Andrey Pautov – 1200km@gmail.com  
- **License:** GPL-3.0-or-later (see [LICENSE](LICENSE)).

Use only in authorized security testing and in compliance with applicable laws.
