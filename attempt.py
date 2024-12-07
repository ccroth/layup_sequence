import sys
sys.setrecursionlimit(2000)

import time
start = time.time()

def S(n: int) -> int:
    if type(n).__name__ != "int" or n < 1:
        raise ValueError(f"Invalid argument \"{n}\": input must be a natural number.")
    if n == 1 or n == 2:
        return n
    else:
        if n%2 == 0:
            res = S(n-1) + S(n-2)
        if n%2 == 1:
            res = 2*S(n-1) - S(n-2)
        return res

print(S(40))

end = time.time()

print(f"Runtime: {end-start} s.")

