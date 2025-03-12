import random
array = [5, 8, 12, 3, 6]
f = random.randint(0, len(array) - 1)
n = [x for i, x in enumerate(array) if i != f]
print("Original array: ",array)
print("Element to exclude: ",array[f])
print("Array after exclusion: ",n)

