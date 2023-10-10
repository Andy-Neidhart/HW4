def my_steps(n: int) -> int:
    if n < 1 or n > 25:
        raise ValueError("Input must be between 1 and 25.")
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        a, b = 1, 2
        for i in range(3, n+1):
            a, b = b, a+b
        return b
