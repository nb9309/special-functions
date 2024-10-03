lst = [i for i in range(1,50)]

z = list(filter(lambda x: x%2 == 0,lst))
y = list(filter(lambda x: x%2 != 0,lst))

print('even numbers: ',z)
print('odd numbers', y)