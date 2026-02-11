# Einfacher CLI-Taschenrechner

A simple command-line calculator written in Python.  
It safely evaluates full mathematical expressions using Python's AST module instead of `eval()`.

---

## Features

- Full expression support (e.g. `3 + 4 * (2 - 1)`)
- Parentheses
- Negative numbers
- Decimal numbers
- Power operator (`**`)
- Error handling (division by zero, invalid input)
- Secure parsing via AST

---

## Design Decisions

- AST-based parsing instead of `eval()` for security
- Functional architecture (no classes required for this scope)
- CLI separated from core logic
- Explicit operator whitelist
- Centralized error handling

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cli-calculator-python.git
cd cli-calculator-python
```

(Optional but recommendet) Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the CLI:

```bash
python main.py
```

Example:

```bash
>> 3 + 4 * 2
= 11

>> (3 + 4) * 2
= 14

>> 10 / 0
= Fehler: Division durch 0
```

Type exit to quit.

---

## Running Tests

This project uses pytest.

Run tests with:

```bash
pytest
```
