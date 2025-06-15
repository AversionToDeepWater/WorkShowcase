'''
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

'''


def rgb(r, g, b):
    # the code below ensures that the values are only between 0 and 255
    ''' e.g. if r was -20:
    r = max(0, min(255, (-20))

    1. min(255, -20) -20 is smaller so 255 is discarded
    2. max (0, -20), 0 is larger so -20 is discarded
    therefore we get r = 0

    e.g. if r was 300

    1. min(255, 300) 255 is smaller so discard 300
    2. max (0, 255), 255 is larger so we discard 0
    therefore r = 255

    this ensures we only have values between 0 and 255
    '''

    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    hex = ('{:02X}' * 3).format(r, g, b)
    return hex