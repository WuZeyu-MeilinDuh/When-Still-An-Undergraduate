#制作可以判断质数的函数。
def prime(num):
    factor = 0
    for i in range(1, num + 1): #利用质数的定义。
        if num % i == 0:
            factor = factor + 1
    if factor == 2:
        return num
    else:
        return False

print('Please enter an integer:')
var = int(input())
print('All prime numbers less than ' + str(var) + ':')
result = []
for t in range(2, var):
    if prime(t) == t:
        result.append(t)
for k in range(0, len(result) - 1):
    print(result[k], end = ',')
print(result[-1])