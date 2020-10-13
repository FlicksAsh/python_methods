tags = ['python', 'development', 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

tags.sort(reverse=True)

print(tags)

totals = [234, 1, 543, 2345]

totals.sort(reverse=True)

print(totals)


# use of sort will yield none if we try to store it in a variable however it will mutate the variable in place 

# if we want to produced a new variable and leave the original alone we must use sorted() 

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)