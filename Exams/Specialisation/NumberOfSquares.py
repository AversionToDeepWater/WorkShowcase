'''

Write a function that finds how many squares are in a X by X grid.
For example a 2x2 Grid has 5 squares:


Non-recursive solution: 6 points
Recursive solution: 12 points
'''

def get_squares(num:int):
    if num == 1:
        return 1
    else:
        return  num * num  + get_squares((num-1))


print(get_squares(2))
print(get_squares(3))