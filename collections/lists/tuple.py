# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable 
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]

print(title)
print(sub_heading)
print(content)



post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))

post += ('published',)

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)


post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']

post += (tags,)

print(post[-1][1])

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[1::2])