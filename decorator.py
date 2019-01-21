#!/usr/bin/python3.7
import datetime
import time
def log(func):
    def wrapper(*args):
        print("functionname:%s"%func.__name__)
        return func(*args)
    return wrapper
@log
def now():
    print(time.localtime())
now()
#equal do log(now)
