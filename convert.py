"""
String format helper for clean and error-free mathematical output.
"""

def format_equation(b, term, n)->str:
    """It Constructs a readable mathematical expression of f(x)."""
    return f"f(x) = {b}*({term})^{n}"

def print_result(var, result) -> None:
    """Prints derivative result in standard notation."""
    print(f"\nDerivative wrt {var}: {result}")
    print("-" * 50)