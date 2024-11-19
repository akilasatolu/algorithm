from typing import List

def merge_sort(b: List[int]) -> List[int]:
    a = b[:]
    if len(a) < 2:
        return a
    m = len(a) // 2
    l = merge_sort(a[:m])
    r = merge_sort(a[m:])
    return merge(l, r)

def merge(l: List[int], r: List[int]) -> List[int]:
    n = []
    while l and r:
        if l[0] < r[0]:
            n.append(l.pop(0))
        else:
            n.append(r.pop(0))
    n.extend(l or r)
    return n

print(merge_sort([2,4,3,0,1]))