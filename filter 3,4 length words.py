lst =[i for i in input().split()]
def fun_name(word):
    if len(word) == 3 or len(word) == 4:
        return True

res = list(filter(fun_name,lst))
print('words in range 3-4 are:',res)


res1 = list(filter(lambda x: len(x)==3 or len(x)==4,lst))
print('By anonymos, words in range of 3,4 are:',res1)