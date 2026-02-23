# Check whether a prime number.
def prime(number):
    prime_base:int = 0
    for i in range(1, number + 1):
        if number % i == 0:
            prime_base += 1
    if prime_base == 2:
        return number
    else:
        return False
#function prime ends.



print('I can tell you all the prime factors of an integer, along with their quantity. Just give me one.')
num = int(input())
prime_list:list[int] = []
for i in range(2, num + 1):
    if num % i == 0 and prime(i) == i:
        prime_list.append(i)
print(prime_list)

times = []
for t in range(0, len(prime_list)):
    base = 0
    while num % prime_list[t] == 0:
        num = num / prime_list[t]
        base += 1
    times.append(base)
print(times)