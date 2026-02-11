import ast
import operator

# --- Architekturentscheidungen ---
# 1. AST-basiertes Parsing statt eval() für Sicherheit
# 2. Nur erlaubte Operatoren implementiert
# 3. Fehlermanagement integriert (ZeroDivision, ungültige Eingabe)
# 4. Einfache, funktionale Struktur, keine Klassen nötig
# 5. CLI bleibt getrennt (main.py)
# ----------------------------------

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def evaluate(node):
    """Rekursives Evaluieren eines AST-Nodes"""
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise TypeError(f"Operator {op_type} nicht erlaubt")
        return OPERATORS[op_type](left, right)
    elif isinstance(node, ast.UnaryOp):
        operand = evaluate(node.operand)
        op_type = type(node.op)
        if op_type not in OPERATORS:
            raise TypeError(f"Operator {op_type} nicht erlaubt")
        return OPERATORS[op_type](operand)
    else:
        raise TypeError(f"Node-Typ {type(node)} nicht erlaubt")

def calculate(expression: str):
    """Berechnet einen Ausdruck. Gibt Fehler als String zurück."""
    try:
        tree = ast.parse(expression, mode='eval')
        return evaluate(tree.body)
    except ZeroDivisionError:
        return "Fehler: Division durch 0"
    except Exception:
        return "Fehler: Ungültige Eingabe"