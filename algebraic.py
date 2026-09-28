"""
Algebraic differentiation:
power rule used for d/dx [b*(var)^n] with step-by-step breakdown
"""


def diffren_algebraic(b, n, var) -> str:
    if b == 0 or n == 0:
        print("\nstep-1: any term with power 0 equals 1")
        return 0
    elif n == 1:
        print(f"\nstep-1: power rule gives {b}*1*{var}^0")
        return f"{b}"
    elif n - 1 == 1:
        print("\nstep-1:",f"{b*n}*{var}^{n-1}")
        return f"{b*n}{var}"
    else:
        print("\nstep-1:",f"{b*n}*{var}^{n-1}")
        return f"{b*n}{var}^{n - 1}"