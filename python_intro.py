# Comment in python
print(1+1)
print(1-1)
print(6+9*3+3)
print(7//2)
print(7%2)
print(6**2)
print(6^2)

# Variables
age = 21
print(age)
a = 1
b = a
a = "Hello, world"
print(a)
print(b)

# Primitive data types are immutable
a = 77
b = a
a = a - 1
print(a)
print(b)

# Lists, dictionaries, and sets are mutable
list_1 = [1, 2, 3]
list_2 = list_1
list_1.append(4)
print(list_1)
print(list_2)

import copy
a = [1, 3, 4, 7]
b = copy.copy(a)
b[0] = -1
print(a)
print(b)

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]
c = [a, b]
d = copy.deepcopy(c)
a[0] = -1
c[0][1] = -3
print(d)

# Object equality
# Check two object have the same values use ==
# Check two object are the same object use is

a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a == c)
print(a is c)
print(a is b)

# Problems with dymanic typing
# a = [1, 2, 3]
# a = 1
# a[0] = 0

# Numeric data types
x = 7
print(type(x))

print(2 + 2.5)
print(int(7/3.5))

x = 7000000000000000000000000000
print(type(x))
print(x)

# Strings
name = "Padraig"
print(type(name))

dialogue = 'Padraig said, "Feck this, I\'m off"\n'
dialogue_2 = ' and then he said, "I\m never coming back"'
print(dialogue + dialogue_2)
print(dialogue * 3)
print(len(dialogue))

# Booleans
collaborative_project_is_fun = True
print(1 > 2)
print(1 < 2 or 2 < 3)
print(1 < 2 or 2 > 3)
print(1 < 2 and 2 > 3)
print(not True)

# Methods
print(name.lower())

# Data structures
# Lists
names = ["Patrick", "Ciaran", "Cian", "Odhran"]
print(names[0])
print(names[3])

random_stuff = [1, 2, 3, "Patrick", True, [1, 2, 3]]
print(random_stuff[-1])

test_numbers = range(10)
for i in range(10):
    print(test_numbers[i])
    



