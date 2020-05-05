import sys
sys.path.append('../../hashtable')
from hashtable import HashTable
import math
import random

slow_table = HashTable()

def slowfun(x, y):
    r = slow_table.get(str((x,y)))
    if r is None:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653

        return v
    return r

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
