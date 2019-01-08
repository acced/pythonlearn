#!/usr/bin/python3.7
import datetime
import time
def log(func):
    def wrapper(*args,**kw):
        print("functionname:%s"%func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print(time.localtime())
now()
