"""
Problem Explanation:

You are given an array that contains n-1 distinct numbers. These numbers are chosen from the range 1 to n, where 
n is the total number of elements you expect. Since there is one missing number, the array contains every number 
from the range except one.

For example, if n = 6, the complete set of numbers would be: [1, 2, 3, 4, 5, 6]
If the array contains the numbers: [1, 2, 3, 5, 6]
Then the missing number is 4.

"""
import random
array = [5, 8, 12, 3, 6]
f = random.randint(0, len(array) - 1)
n = [x for i, x in enumerate(array) if i != f]
print("Original array: ",array)
print("Element to exclude: ",array[f])
print("Array after exclusion: ",n)

