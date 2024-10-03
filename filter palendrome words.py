lst = [word for word in input().split(',')]

z = list(filter(lambda x: x==x[::-1],lst))

print('palendrome words: ',z)