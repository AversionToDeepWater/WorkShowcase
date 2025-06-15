'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))

'''

def zero(arg = None):
    return 0 if not arg else arg(0)

def one(arg = None):
    return 1 if not arg else arg(1)

def two(arg = None):
    return 2 if not arg else arg(2)

def three(arg = None):
    return 3 if not arg else arg(3)

def four(arg = None):
    return 4 if not arg else arg(4)

def five(arg = None):
    return 5 if not arg else arg(5)

def six(arg = None):
    return 6 if not arg else arg(6)

def seven(arg = None):
    return 7 if not arg else arg(7)

def eight(arg = None):
    return 8 if not arg else arg(8)

def nine(arg = None):
    return 9 if not arg else arg(9)

def plus(x):
    add = lambda y : y + x
    return add

def minus(x):
    takeaway = lambda y: y - x
    return takeaway

def times(x):
    multiply = lambda y: x * y
    return multiply

def divided_by(x):
    divide = lambda y: y // x
    return divide
