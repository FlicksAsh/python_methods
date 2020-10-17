# Uniqueness
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags) # will only print coding once 

# Nope
print(tags[0])

query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one) # true 
print(query_two) # false 