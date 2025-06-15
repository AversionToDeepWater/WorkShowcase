'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

'''

def strip_comments(string:str, markers:list) -> str:
    string_list = string.split("\n")
    new_list = []

    for l in string_list:
        for m in markers:
            if m in l:
                l = l.split(m)[0]
        new_list.append(l.rstrip()) #rstrip to remove only trailing


    return "\n".join(new_list)

example = "apples, pears # and bananas\ngrapes\nbananas !apples"

example_result = strip_comments(example, ["#", "!"])

print(example_result)
'''
This doesn't work for edge cases, and also overcomplicates it by going character by character intead of by line
This means it assumes markers will only occur in isolation or one at a time 
def strip_comments(string:str, markers:list) -> str:
    string_list = string.split("\n")
    new_list = []

    for i in string_list:
        new_string = ""
        for char in i:
            if char not in markers:
                new_string += char
            else:
                break 
        new_list.append(new_string.strip())
    
    new_str = "\n".join(new_list)

    return new_str

'''