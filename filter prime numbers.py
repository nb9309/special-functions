lst = [i for i in range(2,100)]
def fun_name(val):
    for j in range(2,(val//2)+1):
        if val%j == 0:
            return False
    return True

z = list(filter(fun_name,lst))
print(z)
