#!/usr/bin/python3.7
import pickle
f=open('p.txt','w')
for x in ['aa',123,'txt']:
    f.write(str(x))
f.close()
f=open('p.txt','r')
xx=f.read()
print('xx=',xx)
f.close()
with opne('test.dat','wb') as fe:l/.
