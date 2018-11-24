import numpy as np

FONT = [[0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0],
        [0,1,1,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
        [0,0,1,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0],
        [0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0],
        [0,0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,0]]

def split_digits(num_str):
    """Converts num_str into an array of 3 x 5 digits"""
    num_digits = len(num_str[0]) // 4
    digits = [ [ x[y*4+1:y*4+4] for x in num_str ] for y in range(num_digits) ]
    return digits

def decode_font(digit, np_font):
    """Takes a 3x5 'digit' and decodes to a number"""
    np_digit = np.array(digit)
    for i, num in enumerate(np_font):
        #Count number of matches and compare to goal
        if np.sum(num != np_digit) <= 1:
            #Logic to handle 0 being at the end of the list
            return 0 if i == 9 else i + 1

def checkio(image):
    np_font = split_digits(FONT)
    digits = split_digits(image)
    num = 0
    for digit in digits:
        res = decode_font(digit, np_font)
        num = num * 10 + res
    return num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "394 clear"
    assert checkio([[0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0],
                    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0]]) == 394, "again 394 but with noise"
