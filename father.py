#!/usr/bin/python3.7
class Person(object):
    __name=None
    __age=None
    def __init__(self,name='zj',age=0):
        self.__name=name
        self.__age=age
    def setname(self,name):
        self.__name=name
    def setage(self,age):
        self.__age=age
    def getname(self):
        return self.__name
    def getage(self,):
        return self.__age
class Student(Person):
    __score=0
    def __init__(self,name='zj',age=0,score=0):
        super().__init__(name,age)
        self.__score=score
    def setscore(self,score):
            self.__score=score
    def getscore(self):
            return self.__score
zhou=Student('zhou')
zhou.setage(22)
zhou.setscore(99)
print('name is %s, age is %d, score is %d'%(zhou.getname(),zhou.getage(),zhou.getscore()))
