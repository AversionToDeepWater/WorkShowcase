"""
Write
def combine()
that combines arrays by alternatingly taking elements passed to it.

E.g

combine(['a', 'b', 'c'], [1, 2, 3]) == ['a', 1, 'b', 2, 'c', 3]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5]) == ['a', 1, 'b', 2, 'c', 3, 4, 5]
combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8]) == ['a', 1, 6, 8, 'b', 2, 7, 'c', 3, 4, 5]
Arrays can have different lengths.

"""
import itertools

def combine(*args) -> list:
    new_combination = []

    for i in itertools.zip_longest(*args):
        new_combination.append(i)

    non_tuple = [j for i in new_combination for j in i if j is not None]

    return non_tuple

test1 = combine(['a', 'b', 'c'], [1, 2, 3])
test2 = combine(['a', 'b', 'c'], [1, 2, 3, 4, 5], [6, 7], [8])

"""
Helpful links:

https://www.geeksforgeeks.org/python/python-iterate-multiple-lists-simultaneously/
https://stackoverflow.com/questions/15269161/in-python-how-to-join-a-list-of-tuples-into-one-list
https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
"""

if __name__ == "__main__":
    print(test1)
    print(test2)