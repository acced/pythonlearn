#!/usr/bin/python3.7
def reversed_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
l1=[x for x in range(8)]
l2=[2,8,3,89,6,5,1]
flag=True
l3=sorted(l2,reverse=True)#Ture means Descending output and if no reverse means asscending output
print(l3)
