# Quick-sort a standard list.(personal try)
def quick_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 0:
        return lst
    else:
        mid = (len(lst)-1) // 2
        pivot = lst[mid]
        left = list()
        right = list()
        for i in lst[0: mid]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        for k in lst[mid + 1: ]:
            if k < pivot:
                left.append(k)
            else:
                right.append(k)
        return quick_sort(left) + [pivot] + quick_sort(right)

# Teacher's version
def quick(lst, low, high):
    i = low
    j = high
    if i >= j:
        return lst
    key = lst[i]
    while i < j:
        while i<j and lst[j] >= key:
            j = j - 1
        lst[i] = lst[j]
        while i<j and lst[i] <= key:
            i = i + 1
        lst[j] = lst[i]
    lst[i] = key
    quick(lst, low, i-1)
    quick(lst, j+1, high)
    return lst

lst = [45,34,12,67,53,55]
print(quick(lst, 0, 5))