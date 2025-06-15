'''
In this kata you will create a function that takes a list of non-negative integers and strings
and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
'''

example = [1,2,'a','b']

def filter_list(l:list)-> list:
    filtered = []
    for item in l:
        if isinstance(item, int): #checks if object fits the data type specified. Checks if it's true/false
            filtered.append(item)
    return filtered

print(filter_list(example))

