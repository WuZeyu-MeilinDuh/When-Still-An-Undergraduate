'''
样例：
xl = [1.5, 2.6, 3.1]
yl = [0.6, 1.3, 2.7]
(x, y) = (1.1, -1)
return 1.5, 0.6
'''

def near_point(xl, yl, x, y):
    distance = [] #distance列表用于储存xl和yl中各点到（x，y）距离的平方。
    for a in range(0, len(xl)):
        distance.append((xl[a] - x)**2 + (yl[a] - y)**2)
    distance_s = [] #创造备用列表来比较大小而不影响原列表distance。
    for c in range(0, len(distance)):
        distance_s.append(distance[c])
    times = []  # 辅助列表，用于记数，判断对应数字是否为“第n大”。
    ylist = []  # ylist用于存储最后的结果（倒序）。
    for t in range(0, len(distance_s)):  # 第几次运行，可以得到第几大的数字。
        for a in range(0, len(distance_s)):
            for b in range(0, len(distance_s)):
                if distance_s[a] >= distance_s[b]:  # 判断a对应的元素是否大于其他元素，大于一次，times中出现次数加一。
                    times.append(distance_s[a])
            if len(times) == len(distance_s) - t:  # 若times元素个数等于xlist中小于等于其的元素个数，则a对应的元素符合要求。
                ylist.append(distance_s[a])
                for i in range(0, len(times)):  # 将times列表清零，准备再次使用。
                    del times[0]
            else:
                for i in range(0, len(times)):  # 将times列表清零，准备再次使用。
                    del times[0]
    tlist = ylist #得到最小距离（的平方）。
    for b in range(0, len(distance)):
        if distance[b] == tlist[-1]: #在distance中找到对应最小距离的点的下标，并存在point中。
            point = b
    answer = (xl[point], yl[point])
    return answer
'''
k = near_point([1.5, 2.6, 3.1],[0.6, 1.3, 2.7], 1.1, -1)
print(k)
'''