# Einfacher CLI-Taschenrechner

## Architekturentscheidungen
- AST-basiertes Parsing für Sicherheit (kein eval)
- Nur mathematisch erlaubte Operatoren (+, -, *, /, **, -)
- Rekursive Funktionsstruktur, kein OOP notwendig
- CLI in eigener Datei, Logik getrennt
- Fehlerbehandlung integriert (ZeroDivision, ungültige Eingaben)

## Features
- Vollständige Ausdrücke
- Negative und Dezimalzahlen
- Klammern
- Division durch 0 abgefangen

## Edge Cases
- Division durch 0
- Leere Eingaben
- Ungültige Zeichen
- Reihenfolge der Operationen korrekt

## Testen
pip install pytest
pytest