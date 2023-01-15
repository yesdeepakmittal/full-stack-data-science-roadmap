from typing import List
def fn(l: List[int]) -> int:
    s: int = 0
    for ele in l:
        s += ele
    return s

# No need to import any stuff here for Python > 3.9
def fn2(l: list[int]) -> int:
    s: int = 0
    for ele in l:
        s += ele
    return s

print(fn([1,2,3,4,5]))
print(fn2([1,2,3,4,5]))