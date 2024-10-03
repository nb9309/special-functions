lst =[float(i) for i in input().split()]

z = list(map(lambda x: x**2,lst))
y = list(map(lambda x: x**0.5, lst))
print('squares of numbers: ',z)
print('square root of numbers: ',y)

# normal fun
def squares(val):
    val = val**2
    return val
def root(val):
    val = val**0.5
    return val

a = list(map(squares,lst))
b = list(map(root,lst))
print(a,b)