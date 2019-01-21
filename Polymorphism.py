#!/usr/bin/python3.7
class Person:
    __name=None
    def __init__(self,name='j'):
        self.__name=name
    def get_name(self):
        return self.__name
    def whoami(self):
        print('i am a person ,My name is ',self.__name)
class Student(Person):
    __score=0
    def __init__(self,name='J',score=0):
        super().__init__(name)
        self.__score=score
    def whoami(self):
        print('i am a student ,My name is %s,My score is %d'%(super().get_name(),self.__score))
class Teacher(Person):
    __title =None
    def __init__(self,name='J',title='none'):
        super().__init__(name)
        self.__title=title
    def whoami(self):
        print('i am a teacher,My name is %s,title is %s'%(super().get_name(),self.__title))
def whoareyou(xx):
    xx.whoami()
p1=Person('zhao')
p2=Student('zhou',90)
p3=Teacher('sun','professor')
whoareyou(p1)
whoareyou(p2)
whoareyou(p3)
