n = int(input())
get_numbers = input()
to_find = [int(x) for x in get_numbers.split()]
ans1 = to_find[0]
ans2 = to_find[1]
if ans1 < ans2:
    ans1, ans2 = ans2, ans1
for i in range(2, n):
    temp = to_find[i]
    if temp > ans1 and ans1 != ans2:
        ans2 = ans1
        ans1 = temp
    elif temp > ans1 and ans1 == ans2:
        ans1 = temp
    elif temp < ans1 and temp > ans2:
        ans2 = temp
print(ans2)