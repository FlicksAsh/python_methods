heading = "Python: An Introduction, and Python: Advanced"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)

first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)

fourth, _, fifth = third.partition(': ')

print(fourth)
print(_)
print(fifth)