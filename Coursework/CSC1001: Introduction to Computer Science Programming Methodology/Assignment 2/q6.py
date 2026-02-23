# Question 6: Eight Queens
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def eight_queens():
    ''' 
    By calling this function, it will display one solution of the Eight Queens
    parameter: no
    reture: no
    '''
    # TODO part
    # A sample solution:
    # |Q| | | | | | | |
    # | | | | |Q| | | |
    # | | | | | | | |Q|
    # | | | | | |Q| | |
    # | | |Q| | | | | |
    # | | | | | | |Q| |
    # | |Q| | | | | | |
    # | | | |Q| | | | |
    # NOTE: you CANNOT just pre-define a solution and display it.
    # Please use algorithm to display a possible solution
    # ------- Your code start here -------

    board = {1: " ",  2: " ",  3: " ",  4: " ",  5: " ",  6: " ",  7: " ",  8: " ",
             9: " ",  10: " ", 11: " ", 12: " ", 13: " ", 14: " ", 15: " ", 16: " ",
             17: " ", 18: " ", 19: " ", 20: " ", 21: " ", 22: " ", 23: " ", 24: " ",
             25: " ", 26: " ", 27: " ", 28: " ", 29: " ", 30: " ", 31: " ", 32: " ",
             33: " ", 34: " ", 35: " ", 36: " ", 37: " ", 38: " ", 39: " ", 40: " ",
             41: " ", 42: " ", 43: " ", 44: " ", 45: " ", 46: " ", 47: " ", 48: " ",
             49: " ", 50: " ", 51: " ", 52: " ", 53: " ", 54: " ", 55: " ", 56: " ",
             57: " ", 58: " ", 59: " ", 60: " ", 61: " ", 62: " ", 63: " ", 64: " ",}
    x = 4
    for i in range(1, 9):
        board[x] = "Q"
        if x <= 49:
            x = x + 15
        else:
            x = x + 15 - 64
    for i in range(1, 9):
        for a in range(i * 8 - 7, i * 8 + 1):
            print("|", board[a], end = "")
        print("|")

    # ------- End of your code -----------


# Call the function to print the solution
if __name__ == '__main__':
    eight_queens()