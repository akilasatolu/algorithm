from typing import List

def linear_search(t: int,l: List[int]) -> int:
    for i in range(len(l)):
        if l[i] == t:
            return i
        i += 1
    return -1

print(linear_search(7, [0,1,2,3,4,5,6,7,8,9]))