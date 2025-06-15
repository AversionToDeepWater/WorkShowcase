'''
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

foobar099 -> foobar100

fo99obar99 -> fo99obar100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

import re
# I think I should try and use re library bc that seems to make the most sense

def increment_string(string: str):#-> str:
    find_num = re.search('.*?([0-9]+)$', string)
    #re. match() searches for matches from the beginning of a string while re.search() searches for matches anywhere in the string.

    if find_num:
        end_num = find_num.group(1) #only gets the numbers from the end of the string
        num_increment = str(int(end_num) + 1).zfill(len(end_num)) #zfill adds leading zeros as those are removed when a string is converted to an int
        #.start() means that the string is sliced at the index of where our end number is found. e.g. "foo042" is sliced at index 3 -> "foo"
        new_str = string[:find_num.start(1)] + num_increment

        #when I used re.match fir find_num, I would get errors bc re.match returns a match object
        #string[:find_num.start(1)] works bc it gets the starting index of group 1
        #start(1) returns an integer which is a valiud index
        return new_str
    else:
        return string + "1"

    # if find:
    #     x = int(find) + 1
    #     return string + " -> " + str(x)












### FIRST ATTEMPT ####
# def increment_string(string):
#     # start at one as we want to increase the number at the end by 1, or add 1 at the end if there isn't a number at the end of the text
#     numbers = []
#     text = ""
#     for i in string: # this only adds one to the first digit it encounters in the string
#         if i.isdigit() or string.endswith(i, i.isdigit()):
#             numbers.append(i)
#         else:
#             text += i
#
#     # string = text + str(numbers)
#
#     return numbers


##### TESTING ####
example1 = "foo1"
#example2 = "foobar"
# example3 = "foobar099"
example4 = "fo99obar99"
example5 = "foo0042"
#
test_output1 = increment_string(example1)
#test_output2 = increment_string(example2)
# test_output3 = increment_string(example3)
test_output4 = increment_string(example4)
test_output5 = increment_string(example5)
print(test_output1)
# # print(test_output2)
print(test_output4)
print(test_output5)




#Articles I looked at

# https://www.w3schools.com/python/python_regex.asp
# https://www.geeksforgeeks.org/python-splitting-text-and-number-in-string/
# https://stackoverflow.com/questions/13518874/python-regex-get-end-digits-from-a-string

'''
USING REGULAR EXPRESSIONS TO FIND INT AT THE END OF A STRING 
(From stack overflow)
>>> import re
>>> s=r"""99-my-name-is-John-Smith-6376827-%^-1-2-767980716"""
>>> re.match('.*?([0-9]+)$', s).group(1)

.*? is a non-greedy match and consumes only as much as possible (a greedy match would consume everything except for the last digit).
[0-9] and \d are two different ways of capturing digits. Note that the latter also matches digits in other writing schemes, like ୪ or ൨.
Parentheses (()) make the content of the expression a group, which can be retrieved with group(1) (or 2 for the second group, 0 for the whole match).
+ means multiple entries (at least one number at the end).
$ matches only the end of the input.

'''





# Code below only works if there is a space between the word and the numbers in the string
# i.e., can split 12 in 'foo 12' but NOT in 'foo12'
# example = 'foo12'
# num = [int(n) for n in example.split() if n.isdigit()]
#
# print(num)

