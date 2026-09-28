"""
Logarithmic differentiation applying the Chain Rule:
d/dx [b*(log(x))^n] with step-by-step breakdown.
"""

def diffren_logarithmic(b, n, var)->str:
    if b == 0 or n == 0:
        print("\nstep-1: any term raised to power 0 equals 1")
        print("step-2: constant differentiation is 0")
        return 0
    
    elif n == 1:
        print(f"\nstep-1: d/dx of log{var} is 1/{var}")
        return f"{b}*(1/{var})"
    elif n - 1 == 1:
        print(f"\nstep-1: {b*n}*log({var})^{n-1}")
        print(f"step-2: multiply by derivative of log({var}) => 1/{var}")
        return f"{b*2}*log({var})*(1/{var})"
    else:
        print(f"\nstep-1: {b*n}*log({var})^{n-1}")
        print(f"step-2: multiply by derivative of log({var}) => 1/{var}")
        return f"{b*n}*(log({var}))^{n-1}*(1/{var})"