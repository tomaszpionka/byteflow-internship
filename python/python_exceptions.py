try:
    f = open('not_found.txt')
except FileNotFoundError:
    print('Sorry. This file does not exist')

try:
    var = bad_var
except Exception:
    print('Variable not found')