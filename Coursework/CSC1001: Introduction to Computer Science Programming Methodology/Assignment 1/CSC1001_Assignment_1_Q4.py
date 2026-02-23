def order(xlist, k):
    times = [] #辅助列表，用于记数，判断对应数字是否为“第n大”。
    ylist = [] #ylist用于存储最后的结果（倒序）。
    for t in range(0, k): #第几次运行，可以得到第几大的数字。
        for a in range(0, len(xlist)):
            for b in range(0, len(xlist)):
                if xlist[a] >= xlist[b]: #判断a对应的元素是否大于其他元素，大于一次，times中出现次数加一。
                    times.append(xlist[a])
            if len(times) == len(xlist) - t: #若times元素个数等于xlist中小于等于其的元素个数，则a对应的元素符合要求。
                ylist.append(xlist[a])
                for i in range(0, len(times)): #将times列表清零，准备再次使用。
                    del times[0]
            else:
                for i in range(0, len(times)): #将times列表清零，准备再次使用。
                    del times[0]
    klist = []
    for s in range(1, k): #这一循环用于将ylist倒着处理一次，得到合题答案。
        klist.append(ylist[-s])
    klist.append(ylist[0])
    return klist #单独最后一项，处理末尾的逗号。