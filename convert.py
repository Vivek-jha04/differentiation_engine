"""
String formatting helper for clean mathematical outputs.
"""

def format_equation(b: int, term: str, n: int) -> str:
    """Constructs a readable mathematical representation of f(x)."""
    return f"f(x) = {b}*({term})^{n}"

def print_result(var: str, result: str) -> None:
    """Prints derivative result in standard notation."""
    print(f"\nDerivative wrt {var}: {result}")
    print("-" * 50)