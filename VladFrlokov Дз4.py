def fibbonachi(n: int) -> list:
    fib_list = [1, 1]
    i = 2
    while i < n:
        for a in range(2, n):
            a = fib_list[a - 1] + fib_list[a - 2]
            fib_list.append(a)
            i = i + 1
    return fib_list
print(fibbonachi(10))