from typing import List

def selection_sort(b: List[int]) -> List[int]:
    a = b[:]
    for i in range(len(a)):
        m = i
        for j in range(i + 1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i] 
    return a

print(selection_sort([2,4,3,0,1]))