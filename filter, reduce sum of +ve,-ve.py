from functools import reduce

lst = [int(i) for i in input().split()]

pos = list(filter(lambda x: x>0,lst))
neg = list(filter(lambda x: x<0,lst))

sum_pos = reduce(lambda x,y:x+y,pos)
sum_neg = reduce(lambda d,n:d+n,neg)
print('pos values: ',pos)
print('sum of +vals: ',sum_pos)
print('neg values: ',neg)
print('sum of -vals: ',sum_neg)