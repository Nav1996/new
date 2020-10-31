import  os
file =open("text.txt",'r')
print(file.read())

"""File handeling first 5 chars"""
import  os
file =open("text.txt",'r')
print(file.read(5))

"""File read lines"""
import  os
file =open("text.txt",'r')
print(file.readline(3))

"""file read over file"""
import os
file=open("text.txt",'r')
for line in file:
    print(file.readlines())
file.close()

"""File writing"""

import os
file = open("text.txt","a")
file.write("this is new")
file.close()

"""file creating"""

import os

file=open("edureka.txt",'x')
file.write("new file edureka")
file.close()

"""delete folder"""

import os
os.remove("edureka.txt")

def func1(name):
    return f"Hello{name}"

def func2(name):
    return f"{name},how you doin?"

def func3(func4):
    return func4('dear learner')

print(func3(func1))
print(func3(func2))

"""functions and inner functions"""

def func():
    print("this is parent functon")
    def func1():
        print("this is first child function")

    def func3():
        print("this is second child function")

    func1()
    func3()

func()

def func(n):

    def func1():
        return "edureka"
    def func3():
        return "python"

    if n==1:
        return func1()
    else:
        return func3()

a=func(1)
b=func(3)

print(a)
print(b)

"""Decoretor"""

def function1(function):
    def wrapper():
        print("hello")
        function()
        print("welcome to edureka")

    return wrapper

def function3():
    print("naveen")

function3=function1(function3)

function3()

@function1

def function3():
    print("naveen")
function3()

def div(a, b):

    return a / b


def smart_dev(func):

    def inner(a, b):

        if a < b:
            a, b = b, a

        return func(a,b)

    return inner

div  =  smart_dev(div)


b=div(9,45)


print(b)




