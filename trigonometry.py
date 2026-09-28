"""
Trigonometric differentiation by using the Chain Rule for
d/dx [b*(trigo(x))^n] with step-by-step solution.
"""

def diffren_trigonometric(b, n, func, var):
    func = func.lower().strip()

    if b == 0 or n == 0:
        print("\nstep-1: we know that constant differentiation or anything multiplied by zero is 0")
        return 0

    
    elif n == 1:
        print(f"\nstep-1: Applying standard derivative for {func}({var})")
        if func == "sin":
            return f"{b}*cos({var})"
        elif func == "cos":
            return f"-{b}*sin({var})"
        elif func == "tan":
            return f"{b}*sec({var})^2"
        elif func == "cot":
            return f"-{b}*cosec({var})^2"
        elif func == "sec":
            return f"{b}*sec({var})*tan({var})"
        elif func == "cosec":
            return f"-{b}*cot({var})*cosec({var})"
        else:
            print('-')
            
            
    
    elif n - 1 == 1:
        bn = b * 2
        if func == "sin":
            print("\nstep-1:", f"{bn}*sin({var})^{n - 1}")
            print("step-2:", f"{bn}*sin({var})^{n - 1}cos{var}")
            return f"{bn}*sin({var})cos({var})"
        elif func == "cos":
            print("\nstep-1:", f"-*{bn}*cos({var})^{n - 1}")
            return f"-*{bn}*cos({var})sin({var})"
        elif func == "tan":
            print("\nstep-1:", f"{bn}*tan({var})^{n - 1}")
            return f"{bn}*tan({var})sec({var})^2"
        elif func == "cot":
            print("\nstep-1:", f"-*{bn}*cot({var})^{n-1}")
            return f"-*{bn}*cot({var})cosec({var})^2"
        elif func == "sec":
            print("\nstep-1:", f"{bn}*sec({var})^{n-1}")
            return f"{bn}*sec({var})^2tan({var})"
        elif func == "cosec":
            print("\nstep-1:", f"-*{bn}*cosec({var})^{n - 1}")
            return f"-*{bn}*cot({var})cosec({var})^2"
        else:
            print('-')

    # General Chain Rule (n > 2 or n < 0)
    else:
        bn = b * n
        if func == "sin":
            print("\nstep-1:", f"{bn}*(sin({var}))^{n-1}")
            return f"{bn}*(sin({var}))^{n-1}(cos{var})"
        elif func == "cos":
            print("\nstep-1:", f"-*{bn}*(cos({var}))^{n-1}")
            return f"-*{bn}*(cos({var}))^{n - 1}sin({var})"
        elif func == "tan":
            print("\nstep-1:", f"{bn}*(tan({var}))^{n-1}")
            return f"{bn}*(tan({var}))^{n-1}*sec({var})^2"
        elif func == "cot":
            print("\nstep-1:", f"-*{bn}*(cot({var}))^{n - 1}")
            return f"-*{bn}*(cot({var}))^{n - 1}*cosec({var})^2"
        elif func == "sec":
            print("\nstep-1:", f"{bn}*(sec({var}))^{n - 1}")
            return f"{bn}*(sec({var}))^{n}*tan({var})"
        elif func == "cosec":
            print("\nstep-1:", f"-*{bn}*(cosec({var}))^{n-1}")
            return f"-*{bn}*(cosec({var}))^{n}*cot({var})"
        else:
            print('-')

       