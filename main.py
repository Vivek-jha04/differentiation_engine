"""
Main output code for Automated Symbolic Differentiation Engine program.
Runs the Interactive Command Line Interface (CLI).
"""

from algebraic import diffren_algebraic
from trigonometry import diffren_trigonometric
from logarithmic import diffren_logarithmic
from constant import diffren_constant
from checks import get_integer_input, validate_trigo_function
from convert import format_equation, print_result

def display_menu():
    print("\n" + "=" * 90)
    print(" "*23 + " AUTOMATED SYMBOLIC DIFFERENTIATION ENGINE")
    print("=" * 90)
    print("1. Algebraic Function (b * x^n)")
    print("2. Trigonometric Function (b * (trigo(x))^n)")
    print("3. Logarithmic Function (b * (log(x))^n)")
    print("4. Constant Function")
    print("5. Quit ('Q')")
    print("-" * 50)

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-5 or Q): ").strip().lower()

        if choice in ['5', 'q', 'quit']:
            print("\nExiting Differentiation Engine. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid selection! Please enter a valid menu number.")
            continue

        # ---------------- 1. ALGEBRAIC ----------------
        if choice == '1':
            var = input("Enter variable name (e.g., x): ").strip() or "x"
            n = get_integer_input("Enter power 'n': ")
            b = get_integer_input("Enter constant multiplier 'b': ")
            
            print(f"\nEquation: {format_equation(b, var, n)}")
            result = diffren_algebraic(b, n, var)
            print_result(var, result)

        # ---------------- 2. TRIGONOMETRY ----------------
        elif choice == '2':
            var = input("Enter angle variable name (e.g., x): ").strip() or "x"
            func = input("Enter trigo function (sin, cos, tan, cot, sec, cosec): ").strip().lower()

            if not validate_trigo_function(func):
                print("Error: Unsupported trigonometric function!")
                continue

            n = get_integer_input("Enter power 'n': ")
            b = get_integer_input("Enter constant multiplier 'b': ")

            print(f"\nEquation: {format_equation(b, f'{func}({var})', n)}")
            result = diffren_trigonometric(b, n, func, var)
            print_result(var, result)

        # ---------------- 3. LOGARITHMIC ----------------
        elif choice == '3':
            var = input("Enter variable name (e.g., x): ").strip() or "x"
            n = get_integer_input("Enter power 'n': ")
            b = get_integer_input("Enter constant multiplier 'b': ")

            print(f"\nEquation: {format_equation(b, f'log({var})', n)}")
            result = diffren_logarithmic(b, n, var)
            print_result(var, result)

        # ---------------- 4. CONSTANT ----------------
        elif choice == '4':
            const_symbol = input("Enter constant symbol/value: ").strip() or "c"
            print(f"\nEquation: f(x) = {const_symbol}")
            result = diffren_constant()
            print_result("x", result)

if __name__ == "__main__":
    main()