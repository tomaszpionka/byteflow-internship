def fibonacci(n):
    a = 0
    b = 1
    print(0)
    for i in range(0,n):
        print(b)
        b += a
        a = b - a

num = 10
fibonacci(num)