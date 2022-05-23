"""
Create a function with two arguments that will return an array of the first (n) multiples of (x).

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array (or list in Python, Haskell or Elixir).

Examples:

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]
"""


# Version 1

def count_by_ver1(x, n):
    final_array = []
    for i in range(n):
        final_array.append(x*(i+1))
    return final_array

# Version 2


def count_by_generator(x, n):
    for i in range(n):
        yield x * (i + 1)


def count_by_ver2(x, n):
    return list(count_by_generator(x, n))

