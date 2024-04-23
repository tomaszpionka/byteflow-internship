try:
    f = open('not_found.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')
