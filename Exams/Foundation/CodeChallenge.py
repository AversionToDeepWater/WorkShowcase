"""
HANDSHAKE CHALLENGE

You will need to:
- Write a function that takes an integer for the number of people and returns an integer with the number of handshakes
- Validate if a handshake can occur given X as an input
- Identify an error state and throw a custom exception
- Create a test file for the function and create a comprehensive test suite

"""
class WrongNumber(ValueError):
    ''' Custom error for wrong value input'''
    pass


def no_of_handshakes(no_people:int) -> int:
    number_handshakes = 0

    if type(no_people) is not int :
        raise WrongNumber('Input must be an integer')
    elif no_people <= 0 :
        raise WrongNumber('Please input a positive integer')
    else:
        number_handshakes = int((no_people * (no_people -1) / 2))
        return number_handshakes


if __name__ == "__main__":
    print(no_of_handshakes(7))

