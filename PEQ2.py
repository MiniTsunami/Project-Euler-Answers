def fibbonaci_even_sum():
    ans = 0
    a = 1
    b = 2
    while a <= 4000000:
        if a % 2 == 0:
            ans += a
        a, b = b, a + b
    return str(ans)


print(fibbonaci_even_sum())