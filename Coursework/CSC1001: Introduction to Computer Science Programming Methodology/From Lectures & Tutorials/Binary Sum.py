def binary_sum(L, start, end):
    if start >= end:
        return 0
    elif start == end-1:
        return L[start]
    else:
        mid = (start + end)//2
        return binary_sum(L, start, mid) + binary_sum(L, mid, end)

L = [1,2,3,4,5,6,7,8,9,10]
print(binary_sum(L, 0, len(L)))