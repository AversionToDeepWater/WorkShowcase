"""
Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""

def solution(string:str) -> str:
    reverse_string = string[::-1]

    return reverse_string

test1 = solution("world")

if __name__ == "__main__":
    print(test1)