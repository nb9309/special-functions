lst = [word for word in input().split(',')]

z = list(map(lambda x: x[::-1],lst))
print('reverse of words: ',z)