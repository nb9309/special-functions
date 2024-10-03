def alphabets(val):
    if val.isalpha():
        return True

def numbers(val):
    if val.isdigit():
        return True

def specialchr(val):
    if not val.isalpha() and not val.isdigit() and not val.isspace():
        return True

lst = [i for i in input().split()]
x = list(filter(alphabets,lst))
y = list(filter(numbers,lst))
z = list(filter(specialchr,lst))

print(''.join(x))
print(''.join(y))
print(''.join(z))

#anonymus function
print('-'*50)
print('By anonymus function')
a = list(filter(lambda x: x.isalpha(),lst))
b = list(filter(lambda x: x.isdigit(),lst))
c = list(filter(lambda x: not x.isalpha() and not x.isdigit() and not x.isspace(),lst))

print(a)
print(b)
print(c)