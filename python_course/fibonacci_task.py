def fibonacci(n):
    a = 0
    b = 1
    for _ in range(0, n):
        print(a)
        b += a
        a = b - a


num = 10
fibonacci(num)
