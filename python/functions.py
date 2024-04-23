def hello_func(greeting, name='You'):
    return f'{greeting}, {name} Function'


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

# hello_func()
# print(hello_func('Hello',name='Bartek').upper())


courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
student_info(*courses, **info)
