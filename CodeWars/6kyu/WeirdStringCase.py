'''
Write a function that accepts a string, and returns the same string with all even indexed characters in each word
upper case, and all odd indexed characters in each word lower cased. The indexing just explained is zero based,
so the zero-ith index is even, therefore that character should be upper case, and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' ').
Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"

'''

string = "This is a test"

## THIS WORKS!! Finally omfg
def to_weird_case(words:str) -> str:
    # len_words = len(words) #no. of characters in words, maybe not needed? -- actually the better way to approach
    # split string at any white space and give you back string as list
    list = words.split()
    result = [ ]

    for word in list:
        weird_case = []
        for i in range(len(word)):
            if i % 2 == 0:
                weird_case.append(word[i].upper())
            else:
                weird_case.append(word[i].lower())
        result.append("".join(weird_case) )#
    str_result = " ".join(result)
    return str_result


    # #for i in list: #So it's zeroth index, each word needs to be considered individually
    # for i in range(len(words)):
    #     if i % 2 == 0 and words[i] != " ":
    #         other_letter.append(words[i].upper())
    #     elif words[i] == " " or i % 2 != 0:
    #         other_letter.append(words[i].lower())
    #     weird_letters = "".join(other_letter) #Do not need to add space to "" bc the space is already in the list
    # return weird_letters


    # for i in range(len(words)):
    #     if i % 2 == 0 and words[i] != " ":
    #          other_letter.append(words[i].upper())
    #     elif words[i] == " " or i % 2 != 0:
    #         other_letter.append(words[i].lower())
    # weird_letters = "".join(other_letter) #Do not need to add space to "" bc the space is already in the list
    # return weird_letters

print(to_weird_case(string))




    # separated = words.split()
    # for i in range(len(separated)):
    #     if i % 2 == 0:
    #         separated[i] = separated[i].upper()
    #     else:
    #         separated[i] = separated[i].lower()
    #     print(i)
    # return separated This just capitalises every other WORD not every other letter




    # for i in words[::2]: # So if I wanted to return every other letter I would use [::2] however, i cannot
    #     # modify the original string using this method as strings are immutable i.e., values cannot be changed
    #     if i != " ": #ignores spaces and commas
    #         i = i.upper()
    #         print(i) #this print statement shows that every other letter is being capitalised
    # # rejoined = " ".join(separated)
    # return words



''' NOTES : use of double colons to slice strings
collection[start:stop:step]
In the syntax above:

collection denotes the data collection (list, string, array, and so on).
start denotes where the slicing operation should start from.
stop denotes where the operation should stop.
step denotes the sequence of iterating through the elements.
If you look closely at the syntax, you can see how the colons separate each parameter.

SOURCE: https://www.freecodecamp.org/news/what-does-mean-in-python-operator-meaning-for-double-colon/
'''



