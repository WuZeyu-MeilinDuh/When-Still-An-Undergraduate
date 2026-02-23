# Question 1: approximate the square root
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def sqrt(n):
    '''
    This function uses Babylonian Method of Computing the Square Root
    parameter n: an int or a float, n >= 0
    reture: an int or a float, the square root of n
    '''
    # TODO part
    # ------- Your code start here -------

    next_guess = 1
    while not -0.000001 < next_guess**2 - n < 0.000001:
        last_guess = next_guess
        next_guess = ( last_guess + ( n / last_guess ) ) / 2
    return next_guess

    # ------- End of your code -----------


# Call the function to approximate the square root
if __name__ == '__main__':
    sqrt(3)
    sqrt(3.3333)
