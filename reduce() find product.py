from functools import reduce
from itertools import product

from mapaddtwolists import lst1

a = reduce(lambda x,y: x*y,lst1)
print('product of values: ',a)

def pro(x,y):
    return x*y

b = reduce(pro,lst1)
print('by normal fun',b)

