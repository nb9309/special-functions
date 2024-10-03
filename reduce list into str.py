from functools import reduce

lst = [i for i in input().split(',')]

s = reduce(lambda x,y:x+' '+y,lst)
print(s)