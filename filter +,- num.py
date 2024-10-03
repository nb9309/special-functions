# filter +ve, -ve numbers from list using normal function
def pos(val):
    if val > 0:
        return True
def neg(val):
    if val < 0:
        return True
lst = [float(i) for i in input().split()]
print(lst)
res = list(filter(pos,lst))
resv = list(filter(neg,lst))
print('postive numbers = ',res)
print('negitive number = ',resv)
