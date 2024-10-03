lst = [int(i) for i in input().split()]

pos = list(filter(lambda x: x>0,lst))
neg = list(filter(lambda x: x<0,lst))

squares = list(map(lambda x:x**2,neg))
roots = list(map(lambda x:x**0.5,pos))

print('neg values: ',neg)
print('squares of -vals: ',squares)
print('pos values: ',pos)
print('roots of +vals: ',roots)