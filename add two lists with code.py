

def add (x,y):
    lst3 = []
    for val1,val2 in zip(x,y):
        lst3.append(val1+val2)

    print(x)
    print(y)
    print(lst3)

lst1 = [float(i) for i in input().split()]
lst2 = [float(i) for i in input().split()]
add(lst1,lst2)