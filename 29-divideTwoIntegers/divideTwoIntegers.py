def divide(dividend, divisor):
    if dividend == divisor:
        return 1

    if dividend == -(2**31) and divisor == -1:
        return (2**31) - 1

    if divisor == 1:
        return dividend

    sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)
    total = 0

    while dividend >= divisor:
        p = 0
        while dividend >= (divisor << p):
            p += 1

        p -= 1
        dividend -= divisor << p
        total += 1 << p

    return min(max(sign * total, -(2**31)), 2**31 - 1)


dividend = 7
divisor = -3

print(divide(dividend, divisor))
