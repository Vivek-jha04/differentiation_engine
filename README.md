# Automated Symbolic Differentiation Engine

This is an automatic and interactive program that calculates the derivatives using (Power Rule and Chain Rule) of algebraic, trigonometry, constant and logarithmic functions.

## Features

- Simple program allowing users to select the function types or quit(Q).
- Algebraic functions: Calculates step-by-step derivative for [b * (var)^n] using Power Rule.
- Trigonometry functions: Calculates derivative for ['sin','cos','tan','cot','sec','cosec'] using the Chain Rule.
- Logarithmic functions Calculates derivative of natural log.
- Constant functions: Derivative gives zero for constant terms.
- Safely handles the error on non-integer inputs or invalid inputs.
 


## Limitations

- For Algebraic functions it only supports "Single-Variable" problems.
- For Trigonometry functions angles "cannot be negative" and it should be "linear".
- For logarithmic functions only support "Single-Variable" inside log, and "negative-variables" inside log is not-defined.


## How to Run

-Clone or download this repository
-Open terminal in the project folder
-Run the program:
=>bash
python main.py

