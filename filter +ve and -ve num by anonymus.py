# filter +ve, -ve numbers from list using anonymus function
lst=[float(i) for i in input().split()]
res = list(filter(lambda x: x>0,lst))
res1 = list(filter(lambda x: x<0, lst))
print('positive numbers of {} : {} '.format(lst,res))
print('negitive numbers of {} : {} '.format(lst,res1))