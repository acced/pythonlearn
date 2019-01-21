#!/usr/bin/python3.7
f=open('p.txt','w')
for x in ['aa',123,'txt']:
    f.write(str(x))
f.close()
f=open('p.txt','r')
xx=f.read()
print('xx=',xx)
f.close()
with open('p.txt','r') as ff:
    x=ff.readline()
    xxx=x[0:-1]
    print('x=',x)
