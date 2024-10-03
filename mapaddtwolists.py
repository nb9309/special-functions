lst1 = [float(i) for i in input().split()]
lst2 = [float(i) for i in input().split()]

z = list(map(lambda x,y: x+y,lst1,lst2))
print(lst1)
print(lst2)
print(z)