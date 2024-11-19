from typing import List

def insertion_sort(b: List[int]) -> List[int]:
    a = b[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print(insertion_sort([2,4,3,0,1]))