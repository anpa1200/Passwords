# Passwords Toolkit

Security testing toolkit for generating wordlists, phone number lists, and Base64-encoded credentials. Intended for **authorized penetration testing and security assessments only**.

## Tools

| Tool | Description |
|------|-------------|
| **PPG** (Personal Pass Generator) | Builds personalized password wordlists from names, dates, nicknames, etc., with 1337 and symbol variants. |
| **phone_numbers_gen** | Generates Israeli phone number lists (configurable prefixes and digit length). |
| **base64_matches** | Produces Base64 `username:password` lines for HTTP Basic Auth / credential testing. |
| **generate_phone_numbers** (C++) | High-performance Israeli phone number generator (same idea as Python, faster for full runs). |

## Requirements

- **Python 3.9+** for all Python tools  
- **C++17 compiler** (e.g. g++, clang++) only for the C++ phone generator  

## Installation

```bash
# Clone and optional editable install
git clone https://github.com/your-repo/Passwords.git
cd Passwords
pip install -e .
# Optional: install dev deps for tests and linting
pip install -e ".[dev]"
```

## Usage

### PPG – Personal Pass Generator

Generates a personalized wordlist (names, dates, symbols, 1337). **Resource note:** with many inputs and options, output can be very large (MB to GB). Prefer 2–5 meaningful entries for typical use.

```bash
# Interactive (prompts for names, dates, options)
python PPG_personal_pass_generator.py

# With options
python PPG_personal_pass_generator.py -o my_list.txt --min-length 6 --max-length 14
```

- `-o, --output` – Output file (default: `special_list.txt`)
- `--min-length`, `--max-length` – Length filter (defaults: 4, 12)
- `--no-interactive` – Only show defaults and exit (no generation)

### Phone number generator (Python)

```bash
# Full Israeli list (default prefixes, 7 digits each)
python phone_numbers_gen.py -o israeli_phone_numbers.txt

# One prefix, limit count (e.g. for testing)
python phone_numbers_gen.py -p 050 -o 050_sample.txt -n 10000

# Custom prefixes
python phone_numbers_gen.py --prefixes 050 052 054 -o mobile.txt -q
```

- `-o, --output` – Output file  
- `-p, --prefixes` – One or more prefixes (default: Israeli mobile/VoIP set)  
- `-d, --digits` – Digits after prefix (default: 7)  
- `-n, --limit` – Stop after N numbers (optional)  
- `-q, --quiet` – No progress to stderr  

### Base64 credential pairs

```bash
# One username, password file
python base64_matches.py -U admin -p passwords.txt -o matches_base64.txt

# Username list × password list
python base64_matches.py -u usernames.txt -p passwords.txt -o matches_base64.txt

# Interactive (no args)
python base64_matches.py
```

- `-U, --username` – Single username  
- `-u, --usernames` – File with one username per line  
- `-p, --passwords` – File with one password per line  
- `-o, --output` – Output file (default: `matches_base64.txt`)  

### C++ phone number generator

```bash
make cpp
./generate_phone_numbers                    # writes israeli_phone_numbers.txt
./generate_phone_numbers /path/to/out.txt   # custom output path
```

## Resource usage (PPG)

With **all** options and many inputs, PPG can produce very large wordlists (up to TB range) and use significant CPU/memory. For practical use:

- Prefer **2–5** high-value entries (e.g. name, birthdate, nickname).  
- Use `--min-length` and `--max-length` to cap size and relevance.  
- Monitor disk space when writing the output file.  

## License and author

- **Author:** Andrey Pautov – 1200km@gmail.com  
- **License:** GPL-3.0-or-later (see [LICENSE](LICENSE)).  

Use only in authorized security testing and in compliance with applicable laws.
