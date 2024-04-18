def foobar(n):
    for number in range(0, n):
        if (number % 3 == 0) and (number % 5 == 0):
            print('foobar')
        elif number % 5 == 0:
            print('bar')
        elif number % 3 == 0:
            print('foo')
        else:
            print(number)


num = 100
foobar(num)
