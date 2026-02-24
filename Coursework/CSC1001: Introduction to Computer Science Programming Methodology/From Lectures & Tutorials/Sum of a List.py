def linear_sum(L, n):
    if n < 0:
        return 0
    else:
        return L[n-1] + linear_sum(L, n-1)