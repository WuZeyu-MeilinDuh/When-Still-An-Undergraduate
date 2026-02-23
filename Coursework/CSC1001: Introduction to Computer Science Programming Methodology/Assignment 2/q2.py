# Question 2: Emirp
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary


def display_emirps(n):
    '''
    By calling this function, it will print the first n emirps
    It will display 10 numbers per line and align the numbers
    parameter n: int, n > 0
    reture: no
    '''
    # TODO part
    # ------- Your code start here -------
    lst = []
    t = 12
    while len(lst) < n:
        if palindromic(t) != t:
            s = palindromic(t)
            if confirm_prime(s) == s and confirm_prime(t) == t:
                lst.append(t)
        t = t + 1
    leng = len(lst)
    a = leng // 10
    b = leng % 10
    for i in range(1, a + 1):
        for y in range((i - 1) * 10, i * 10):
            print(lst[y], "\t",end = " ")
        print("\n")
    for c in range(b ,1, -1):
        print(lst[-c], "\t",end = " ")
    if b != 0:
        print(lst[-1])

def palindromic(m):
    integ = str(m)
    num = ""
    for i in range(len(integ) - 1, -1, -1):
        num = num + str(integ[i])
    n = int(num)
    return n

def confirm_prime(k):
    time = 0
    for i in range(2, k):
        if k % i == 0:
            time += 1
    if time == 0:
        return k
    else:
        return False
    
    # ------- End of your code -----------


# Call the function to print the first n emirps
if __name__ == '__main__':
    display_emirps(10)
    display_emirps(55)