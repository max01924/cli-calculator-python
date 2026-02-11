# Einfacher CLI-Taschenrechner

## Architekturentscheidungen
- AST-basiertes Parsing für Sicherheit (kein eval)
- Nur mathematisch erlaubte Operatoren (+, -, *, /, **, -)
- Rekursive Funktionsstruktur, kein OOP notwendig
- CLI in eigener Datei, Logik getrennt
- Fehlerbehandlung integriert (ZeroDivision, ungültige Eingaben)

## Features

- Full expression support (e.g. `3 + 4 * (2 - 1)`)
- Parentheses
- Negative numbers
- Decimal numbers
- Power operator (`**`)
- Error handling (division by zero, invalid input)
- Secure parsing via AST

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cli-calculator-python.git
cd cli-calculator-python

(Optional but recommended) Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
