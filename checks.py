"""
Input valid checking for the Differentiation Engine.
Handles valueError and menu choices.
"""

def get_integer_input(prompt: str) -> int:
    """Prompt user until a valid integer is provided."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Input must be a valid integer! Please try again.")

def validate_trigo_function(func_name: str) -> bool:
    """Check if the provided function is a supported trigonometric operation."""
    valid_func = {"sin", "cos", "tan", "cot", "sec", "cosec"}
    return func_name.lower().strip() in valid_func