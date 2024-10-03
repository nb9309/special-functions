lst = [word for word in input().split(',')]

z = list(filter(lambda x: x[0] == x[-1],lst))
print('starts and end with same letter: ',z)