# For loop over a list 
names = ['John', 'Mary', 'Bob']
for name in names:
  print(name)

# List comprehension to capture even numbers
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# Unpacking dictionary
person = {'name': 'John', 'age': 30}
for key, value in person.items():
  print(key, value)

#----------------------------------------

# Separate items into different lists
nums = [1, 2, 3, 4, 5, 6]
evens = []
odds = []

for n in nums:
  if n % 2 == 0:
    evens.append(n)
  else:
    odds.append(n)

print("Even numbers:", evens)
print("Odd numbers:", odds)
