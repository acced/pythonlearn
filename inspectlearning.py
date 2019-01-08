#!/usr/bin/python3.7
import inspect
def get_current_function_name():
    functionname=inspect.stack()
    print("enter {}()".format(functionname))
def say_hello():
    get_current_function_name()
    print("Hello")
say_hello()
