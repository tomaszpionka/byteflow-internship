language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'Javascript':
    print('Language is Javascript')
else:
    print('No match')

user = 'Admin'
logged_in = False
# Logic operators and/or
if user == 'Admin' or logged_in:
    print('Admin page')
else:
    print('Bad credentials')

if not logged_in:
    print("Please log in")
else:
    print('Welcome')

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)

condition = {}
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')