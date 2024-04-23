student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']}

#student['phone'] = '555-555-555'
#del student['age']
#age = student.pop('age')

print(student)
#print(age)
print(student['name'])
print(student.get('phone','Not Found'))
for key in student:
    print(key)