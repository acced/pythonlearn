#!/usr/bin/python3.7
from functools import reduce
def f2(x):
    return x*x
l1=[1,2,3,4,5,6,7,8]
l2=[x for x in range(8)]
l3=list(map(f2,l1))#map output in iterator
print(l3)
def f3(x,y):
    return x*y
l4=reduce(f3,l1)#find reduce is in the package functool and need two variable
print(l4)
def is_odd(n):
    return n%2==1
print(list(filter(is_odd,l3)))
