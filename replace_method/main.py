sentence = 'The quick brown fox jumped over the lazy dog.'

sentence = sentence.replace('quick', 'slow')

print(sentence.replace('quick', 'slow'))
print(sentence)

# Doesn't actually change the pointer for the string since strings are immutable in python which makes it good for data science since you can have confidence your data hasn't changed 


