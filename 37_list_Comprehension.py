# List Comprehension = A concise way to create lists in python compact 
#  Compact and easier to read them traditional loops 
#  [expression for value in iterable if condition]

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

print(squares)

grades = [85,42,79,90,56,61,30]
passing_grades = [grade for grade in grades if grade >= 60]


print(passing_grades)