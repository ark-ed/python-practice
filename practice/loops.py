# Loops practice
# Finding the biggest number from a list
# Mosh's Solution

list = [5, 8, 14, 3, 1, 9, 2, 61, 6, 6, 3, 25, 14, 18, 21, 28, 31, 15, 29, 35, 39, 40, 41, 28, 41]

i = list[0] # Assuming the first value in the list is the largest value
for v in list:
  if i < v: # Compares i to the next value in the list
    i = v # If i is less than v, it will set i to v: The larger number

print(f"The greatest number in the list is {i}")