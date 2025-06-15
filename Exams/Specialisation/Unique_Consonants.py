'''
2.1 A) Write a function that takes in a string and returns the number of
unique consonants [10 marks]
EXAMPLE INPUT: “cat”
EXAMPLE OUTPUT: 2 (‘c’ and ‘t’ are both unique)
EXAMPLE INPUT: “cataract”
EXAMPLE OUTPUT: 1 (‘r’ is the only unique consonant)

B) What is the time and space complexity of your solution?
If you are making any assumptions in your calculations, list them.
[2 marks]

'''

from collections import Counter


def unique_consonants(string:str):
    c_number = 0
    lower_case = string.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = []

    for i in lower_case:
        if i not in vowels and i.isalpha():
            consonants.append(i)

    count = Counter(consonants)

    for i in count:
        if count[i] == 1:
            c_number += 1
    return c_number


print(unique_consonants("cat"))
print(unique_consonants("cataract"))

#TIME COMPLEXITY is O(n)
# This is as I am using a for loop to iterate through n elements in a string assuming there are no spaces in the string
#SPACE COMPLEXITY is O(1)
# This is as I get a single int returned