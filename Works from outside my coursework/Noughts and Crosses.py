board = {"tl": " ", "tm": " ", "tr": " ",
         "ml": " ", "mm": " ", "mr": " ",
         "dl": " ", "dm": " ", "dr": " "}

def display(board):
    print(board["tl"] + "|" + board["tm"] + "|" + board["tr"])
    print("-+-+-")
    print(board["ml"] + "|" + board["mm"] + "|" + board["mr"])
    print("-+-+-")
    print(board["dl"] + "|" + board["dm"] + "|" + board["dr"])

print(" ")
print("This is an example for your reference to move:")
print(" ")
example = {"tl": "tl", "tm": "tm", "tr": "tr",
           "ml": "ml", "mm": "mm", "mr": "mr",
           "dl": "dl", "dm": "dm", "dr": "dr"}
print(example["tl"] + "|" + example["tm"] + "|" + example["tr"])
print("--+--+--")
print(example["ml"] + "|" + example["mm"] + "|" + example["mr"])
print("--+--+--")
print(example["dl"] + "|" + example["dm"] + "|" + example["dr"])
print(" ")
print("Would you like to play?(yes or no)")
reply = input()
if reply == "yes":
    print(" ")
    turn = "X"
    for i in range(9):
        print(" ")
        print("This move of " + turn + " is to be placed in ?")
        move = input()
        board[move] = turn
        print(" ")
        display(board)

        if board["tl"] == board["tm"] and board["tl"] == board["tr"] and board["tl"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["ml"] == board["mm"] and board["ml"] == board["mr"] and board["ml"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["dl"] == board["dm"] and board["dl"] == board["dr"] and board["dr"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["tl"] == board["ml"] and board["ml"] == board["dl"] and board["dl"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["tm"] == board["mm"] and board["mm"] == board["dm"] and board["mm"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["tr"] == board["mr"] and board["mr"] == board["dr"] and board["mr"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["tl"] == board["mm"] and board["mm"] == board["dr"] and board["dr"] != " ":
            print("Player of " + turn + " has won.")
            break
        elif board["tr"] == board["mm"] and board["mm"] == board["dl"] and board["dl"] != " ":
            print("Player of " + turn + " has won.")
            break

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
else:
    print("Programme ended.")