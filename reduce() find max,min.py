from functools import reduce

lst = [float(i) for i in input().split()]

amax = reduce(lambda x,y: x if x>y else y,lst)
amin = reduce(lambda x,y: x if x<y else y, lst)

print('highest word: ',amax)
print('smallest word: ',amin)