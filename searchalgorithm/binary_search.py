from typing import List

def binary_search(t: int,b: List[int]) -> int:
    a = b[:]
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if t == a[m]:
            return m
        elif t > a[m]:
            l = m + 1
        else:
            r = m - 1
    return -1

print(binary_search(7, [0,1,2,3,4,5,6,7,8,9]))