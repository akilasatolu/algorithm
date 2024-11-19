from typing import List

def bubble_sort(b: List[int]) -> List[int]:
    a = b[:]
    for i in range(len(a) - 1, 0, -1):
        swapped = False
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a

print(bubble_sort([2,4,3,0,1]))