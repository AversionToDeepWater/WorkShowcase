"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will
be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit
and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

EXAMPLES
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1

HELP
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+


"""

class RomanNumerals:
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym = ["I", "IV","V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]



    @staticmethod
    def to_roman(val : int) -> str:
        result = ""
        i = 12
        while val:
            div = val // RomanNumerals.num[i]
            val %= RomanNumerals.num[i]

            while div:
                result += RomanNumerals.sym[i]
                div -= 1  #so we add the relevant roman numeral the correct number of times
            i -= 1
        return result


    @staticmethod
    def from_roman(roman_num : str) -> int:
        #here we have made a dictionary of the roman numerals with their corresponding numbers
        roman_dict = dict(zip(RomanNumerals.sym, RomanNumerals.num))

        i = 0
        num = 0
        while i < len(roman_num): #this ensures we can only traverse through the length of the string input

            #the first if statement checks to see if there is a two character roman value
            # this is by making sure we 1. are not out of bounds of the length of the string
            # and 2. that the two character roman numeral exists in the dictionary
            if i + 1 < len(roman_num) and roman_num[i:i+2] in roman_dict:
                num += roman_dict[roman_num[i:i+2]]
                i += 2 #as we have covered two characters in the string i+2
            else:
                num += roman_dict[roman_num[i]]
                i+= 1


        return num

number = 3549
test = 2008
roman = 'MMMDXLIX'
print("Roman value of number is:", RomanNumerals.to_roman(test))
#print("The integer value is: ", RomanNumerals.from_roman(roman))

'''
Useful info: https://www.geeksforgeeks.org/python-program-to-convert-integer-to-roman/

'//' is a floor division operator. 
This means after it divides two numbers, it returns the largest integer less than or equal to the result
e.g. 7 // 2 = 3. This is as 7/2 = 3.5, meaning 3 is the largest int smaller than 3.5

'%' is the modulus operator.
This means it divides two numbers and returns the remainder of the division.
e.g. 7 %2 = 1, where 1 is the remainder after the division.

'''