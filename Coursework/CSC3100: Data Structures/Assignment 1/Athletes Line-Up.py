# Inefficient tries in quotes

'''from operator import index

n = int(input())
line_info = input()
ori_line = [int(x) for x in line_info.split()]
swap_times = 0
temp = sorted(ori_line)
for i in range(n):
    k = temp[i]
    m = ori_line.index(k)
    ori_line[m] = i + 1
for i in range(n):
    target = i + 1
    if ori_line[i] != target:
        ind_target = ori_line.index(target)
        ori_line[i], ori_line[ind_target] = target, ori_line[i]
        swap_times = swap_times + 1
    else:
        continue
print(swap_times)'''

'''n = int(input())
line_info = input()
ori_line = [int(x) for x in line_info.split()]

def q_s(lis, lengt, lef, righ):
    if lengt == 1:
        return 0
    else:
        swap_times = 0
        i = lef
        j = righ
        piv = lis[lef]
        while i != j:
            if ori_line[j] > piv:
                j = j - 1
            elif ori_line[j] < piv:
                while ori_line[i] <= piv and i != j:
                    i = i + 1
                if i != j:
                    ori_line[i], ori_line[j] = ori_line[j], ori_line[i]
                    swap_times = swap_times + 1
                else:
                    pass
        ori_line[lef], ori_line[i] = ori_line[i], ori_line[lef]
        swap_times = swap_times + 1
        return q_s(lis, lengt//2, lef, lengt//2 - 1) + q_s(lis, lengt//2, lengt//2+1, righ) + swap_times

tim = q_s(ori_line, n, 0, n-1)
print(tim)'''

'''n = int(input())
line_info = input()
ori_line = [int(x) for x in line_info.split()]
swap_times = 0
sor = sorted(ori_line)
for i in range(n):
    if ori_line[i] == sor[i]:
        pass
    else:
        swap_times = swap_times + 1
if swap_times/2 == swap_times//2:
    print(int(swap_times/2))
else:
    print(int(swap_times//2 + 1))'''


def solve():

    n = int(input())
    input_data = input().split()
    a = list(map(int, input_data[:]))

    nodes = []
    for i in range(n):
        nodes.append([a[i], i])

    nodes.sort()

    visited = [False] * n
    min_swaps = 0

    for i in range(n):
        if visited[i] or nodes[i][1] == i:
            continue

        cycle_size = 0
        curr = i

        while not visited[curr]:
            visited[curr] = True
            curr = nodes[curr][1]
            cycle_size += 1

        if cycle_size > 0:
            min_swaps += (cycle_size - 1)

    print(min_swaps)

solve()