courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']
#courses.append('Art')
#courses.insert(0,'Art')
# Adding multiple elements to the list
courses.extend(courses_2)

#popped = courses.pop()

# Sorting
#courses.sort(reverse=True)
sorted_courses = sorted(courses)

print(courses.index('CompSci'))
print('Art'in courses)

#for loops
for item in enumerate(courses, start=1):
    print(item)

# String joining
course_str = '-'.join(courses)
new_list = course_str.split('-')

print(new_list)
print(course_str)

# Tuples
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

# Sets
cs_courses = {'History','Math','Physics','CompSci','Math'}
print(cs_courses)
'''
print(courses)
print(sorted_courses)

print(popped)
print(courses[-1])
print(courses[0:2])
'''