def prime():
    for i in range(2,100):
        res = True
        for j in range(2,i//2+1):
            if i%j == 0:
                res = False
                break

        if res:
            print(i,end=' ')

prime()