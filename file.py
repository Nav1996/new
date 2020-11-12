# import  os
# file =open("text.txt",'r')
# print(file.read())
#
# """File handeling first 5 chars"""
# import  os
# file =open("text.txt",'r')
# print(file.read(5))
#
# """File read lines"""
# import  os
# file =open("text.txt",'r')
# print(file.readline(3))
#
# """file read over file"""
# import os
# file=open("text.txt",'r')
# for line in file:
#     print(file.readlines())
# file.close()
#
# """File writing"""
#
# import os
# file = open("text.txt","a")
# file.write("this is new")
# file.close()
#
# """file creating"""
#
# import os
#
# file=open("edureka.txt",'x')
# file.write("new file edureka")
# file.close()
#
# """delete folder"""
#
# import os
# os.remove("edureka.txt")
#
# def func1(name):
#     return f"Hello{name}"
#
# def func2(name):
#     return f"{name},how you doin?"
#
# def func3(func4):
#     return func4('dear learner')
#
# print(func3(func1))
# print(func3(func2))
#
# """functions and inner functions"""
#
# def func():
#     print("this is parent functon")
#     def func1():
#         print("this is first child function")
#
#     def func3():
#         print("this is second child function")
#
#     func1()
#     func3()
#
# func()
#
# def func(n):
#
#     def func1():
#         return "edureka"
#     def func3():
#         return "python"
#
#     if n==1:
#         return func1()
#     else:
#         return func3()
#
# a=func(1)
# b=func(3)
#
# print(a)
# print(b)
#
# """Decoretor"""
#
# def function1(function):
#     def wrapper():
#         print("hello")
#         function()
#         print("welcome to edureka")
#
#     return wrapper
#
# def function3():
#     print("naveen")
#
# function3=function1(function3)
#
# function3()
#
# @function1
#
# def function3():
#     print("naveen")
# function3()
#
# def div(a, b):
#
#     return a / b
#
#
# def smart_dev(func):
#
#     def inner(a, b):
#
#         if a < b:
#             a, b = b, a
#
#         return func(a,b)
#
#     return inner
#
# div  =  smart_dev(div)
#
#
# b=div(9,45)
#
#
# print(b)
#
#
#

# def add_sub(x,y):
#
#     c=x+y
#     d=x-y
#     return c,d
#
# result1,result=add_sub(10,5)
#
# print(result1,result)


a=(3,1,7)
b=(8,1,4)
#
# def compareTriplets(a,b):
#
#     aliceMark = 0
#     bobMark = 0
#
#     for i in range(0,3):
#         if a[i]>b[i]:
#             aliceMark+=1
#         elif a[i]==b[i]:
#             pass
#         else:
#             bobMark+=1
#
#     return aliceMark,bobMark
#
# result = compareTriplets(a,b)
#
# print("alice mark is :",result)
# from array import *
# def aVerybigSum(ar):
#
#     sumLong =0
#
#     lenar=len(ar)
#
#     for i in range(0,lenar):
#         sumLong+=ar[i]
#
#     return sumLong
#
# sum = array('i',[988,8808,8898])
#
# print(aVerybigSum(sum))

import sys
#
#
# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)
#
# def diagonalDifference(arr):
#
#     n=0
#     max=len(arr)
#     sum_p=0
#     sum_s=0
#     sum=0
#
#     for i in range(0,max):
#         sum_p+=arr[i][i]
#         sum_s+=arr[i][max-1]
#
#
#         max-=1
#
#     if(sum_s-sum_p>0):
#         sum =sum_s-sum_p
#     else:
#         sum=sum_p-sum_s
#
#     return sum
#
# print(a)
# print(diagonalDifference(a))
#
# from array import *
#
# a = array('i',[-1,3,4,0,0,-3])
#
# def plusMinus(arr):
#
#     lenarr=len(arr)
#     plus=0
#     negative=0
#     zero=0
#
#     for i in range (0,lenarr):
#
#         if arr[i]>0:
#             plus+=1
#         elif arr[i]<0:
#             negative+=1
#         else:
#             zero+=1
#
#     print(str(plus/lenarr).format('{0:.6f}', 2))
#     print(str(negative/lenarr).format('{0:.6f}', 2))
#     print(str(zero/lenarr).format('{0:.6f}', 2))
#
# plusMinus(a)

# for i in range(4):
#
#     for j in range(4-i):
#         print(" ",end="")
#
#     for m in range(i+1):
#         print("#",end="")
#
#     print()

"""sum of four out of 5"""

from array import *

a = array('i',[100,1,3,9,-8])

# minimum =a[0]
# maximum=a[0]
# sum =0
#
# for i in range(5):
#
#     sum+=a[i]
#
#     if minimum>a[i]:
#         minimum=a[i]
#
#     if maximum<a[i]:
#         maximum=a[i]
#
# print(sum-maximum,sum-minimum)
#
# def birthdayCakeCandles(candles):
#     highest = candles[0]
#     count = 0
#     lencandles=len(candles)
#
#     for i in range(lencandles):
#
#         if highest < candles[i]:
#             highest = candles[i]
#
#
#     for i in range(lencandles):
#         if highest == candles[i]:
#             count += 1
#
#     return count
#
# candles=array('i',[3,1,3,3,7,7,7,9])
#
# print(birthdayCakeCandles(candles))
#
# str3="12:40:22AM"
#
# if(str3[8:11]=='AM'and str3[0:2]=='12'):
#
#     newstr = str3[2:8]
#     print('00'+newstr)
#
# elif(str3[8:11]=='AM'and str3[0:2]!='12'):
#
#     print(str3[0:8])
#
# elif(str3[8:11]=='PM'and str3[0:2]=='12'):
#
#     print(str3[0:8])
#
# else:
#     newstr =str3[2:8]
#     num=int(str3[0:2]) + 12
#     str1=str(num)
#     print(str1+newstr)
#
# class square:
#
#     def __init__(self,side):
#         self._side=side
#
#     @property
#     def side(self):
#         return self._side
#
#     @side.setter
#     def side(self,value):
#         if value>=0:
#             self._side=value
#         else:
#             print("error")
#
#     @property
#     def area(self):
#         return self._side**2
#
#     @classmethod
#     def unit_square(cls):
#         return cls(1)
#
# s=square(5)
# print(s.side)
# print(s.area)
#
#
# """sinsgleton class"""
#
# import functools
# def singelton(cls):
#
#     @functools.wraps(cls)
#     def wrapper(*args,**kwargs):
#         if not wrapper.instance:
#             wrapper.instace=cls(*args,**kwargs)
#         return wrapper.instance
#     wrapper.instance=None
#     return wrapper
# @singelton
# class one:
#     pass
#
# first=one()
# second=one()
#
# print(first is second)
#
# """lamda functions"""
#
# x=lambda a:a*a
#
# print(x(3))
#
# def A(x):
#     return (lambda y:x+y)
#
# t=A(4)
# t(8)
# print(t(8))
#
# """lamda within filter"""
#
# mylist = [1,3,4,5,6,7]
#
# newlist=list(filter(lambda a:(a/3==2),mylist))
#
# print(newlist)
#
# """lamda within map"""
# mylist = [1,3,4,5,6,7]
#
# newlist=list(map(lambda a:(a/3 !=2),mylist))
#
# print(newlist)
#
# """lamda within reduce"""
#
# from functools import reduce
#
# x=reduce(lambda a,b:a+b,[34,54,4,65,75])
# print(x)
#
# """solving algebric expression using lamda"""
#
# s=lambda a:a*a
#
# print(s(4))
#
# d=lambda x,y:3*x+4*y
#
# print(d(4,7))
# """check password strength"""
# password="1z2!"
#
# def minimumNumber(password):
#     numbers = "0123456789"
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     special_characters = "!@#$%^&*()-+"
#
#     ncount = 0
#     lcount = 0
#     ucount = 0
#     scount = 0
#     lenp = len(password)
#     reqnumber=0
#
#     if lenp <= 4:
#         return 6 - lenp
#
#     else:
#
#         for i in range(0,lenp):
#
#             for j in range(0,10):
#
#                 if password[i] == numbers[j]:
#                     ncount += 1
#
#             for q in range(0,26):
#                 if password[i]==lower_case[q]:
#                     lcount+=1
#
#                 if password[i]==upper_case[q]:
#                     ucount+=1
#
#             for r in range(0,12):
#
#                 if password[i]==special_characters[r]:
#                     scount+=1
#
#
#         if(ncount!=0 and lcount!=0 and ucount!=0 and scount!=0 and lenp<=6):
#
#             reqnumber =6-lenp
#
#         if (ncount != 0 and lcount != 0 and ucount != 0 and scount != 0 and lenp > 6):
#
#             reqnumber =0
#
#         if(ncount==0):
#             reqnumber+=1
#         if (lcount == 0):
#             reqnumber += 1
#         if (ucount == 0):
#             reqnumber += 1
#         if (scount == 0):
#             reqnumber += 1
#
#         if lenp+reqnumber<6:
#             reqnumber=6-reqnumber+lenp
#
#     return reqnumber
#
#
# print(minimumNumber(password))
#
# """Dividors"""
#
# def findDigits(n):
#
#     digits=[int(x) for x in str(n)]
#     count=0
#
#     for i in range(len(digits)):
#
#         if n%digits[i]==0:
#             count+=1
#
#     print(count)
#
# findDigits(1426)

# n=int(input())
#
# for i in range(1,n+1):
#     print(i, end="")
#
# def fact(n):
#
#     if(n==0):
#         return 1
#
#     # a[] = n*fact(n-1)
#
#
#     return a
#
# result=fact(10)
# print(result)
#
# a=8683849840*546364756
# print(a)

# """filter with map"""
#
# c=map(lambda x:x+x,filter(lambda x:(x>=4),[5,65,3,13,1,1]))
#
# print(list(c))

# """map within filter"""
#
# d = filter(lambda x: (x >= 10),map(lambda x : (x-4),[9,6,7,5,1,99,78]))
#
# print(list(d))
#
# """reduce within map and filter"""
#
# from functools import reduce
#
# d = reduce(lambda x,y:(x+y),filter(lambda x: (x >= 10),map(lambda x : (x-4),[9,6,7,5,1,99,78])))
#
# print(d)

# def migratoryBirds(arr):
#     maxcount = 0
#     num = arr[0]
#
#     for i in arr:
#
#         freq = arr.count(i)
#
#         if freq > maxcount:
#             maxcount = freq
#             num = i
#
#     return num
#
# arr=[1,3,4]

# print(migratoryBirds(arr))

#
# def bonAppetit(bill, k, b):
#
#     sumbill=0
#     a=0
#
#     for i in range(len(bill)):
#
#         sumbill+=bill[i]
#
#     sumbill-=bill[k]
#
#     if(sumbill-b==0):
#         return "Bon Appetit"
#
#     else:
#         a=b-
#         return a
#
# bill=[3,10,2,9]
#
# bonAppetit(bill,1,12)

# print(int(3/6))

from collections import Counter

# def sockMerchant(ar):
    #
    # paircount = 0
    # sockcount=0
    # uniquelist=[]
    #
    # def unique(ar):
    #
    #     for x in ar:
    #
    #         if x not in uniquelist:
    #             uniquelist.append(x)
    #
    # unique(ar)
    #
    # for i in uniquelist:
    #
    #     sockcount=ar.count(i)
    #
    #     if sockcount>=2:
    #         paircount+=int(sockcount/2)
    #
    #
    # return paircount
#
# ar=[3,3,4,5,4,6,7,8,9,0]
#
# print(sockMerchant(ar))


# from array import *
#
# arr = array('i',[])
#
# n=int(input("Enter number of elements: "))
#
# for i in range(n):
#
#     x=int(input("Enter the next value"))
#     arr.append(x)
#
# print(arr)
#
# to_beSearched=int(input("Enter the number for search"))
#
# for i in range(n):
#     if(to_beSearched==arr[i]):
#         print("value available in: ",i)
#
# class computer:
#
#     def __init__(self,cpu,ram):
#         self.cpu=cpu
#         self.ram=ram
#
#     def config(self):
#         print("i5 with 16gb ram",self.cpu,self.ram)
#
# com1 = computer('i5',8)
#
# com1.config()

# """constructor"""
#
# class Computer:
#
#     def __init__(self):
#         self.name='naveen'
#         self.age=38
#
#     def update(self):
#         self.age=30
#
#
# c1=Computer()
# c2=Computer()
#
# print(id(c1),id(c2))
# print(c1.name)
# print(c2.name)
# c1.name='nivantha'
# print(c1.name)
# print(c2.name)

# class car:
#
#     wheels=4
#
#     def __init__(self):
#         self.mil
#         self.name
#
# class Student:
#
#     school='naveen'
#
#     def __init__(self,m1,m3,m4):
#
#         self.m1=m1
#         self.m3=m3
#         self.m4=m4
#
#     def avg(self):
#         return (self.m1+self.m3+self.m4)/3
#
#     def get_m1(self):
#         return self.m1
#     def set_m1(self,value):
#         self.m1=value
#
#     @classmethod
#     def info(cls):
#         return cls.school
#
#     @staticmethod
#     def new():
#         print("new static function")
#
# s1 = Student(13,4,3)
# s3 = Student(13,4,3)
# s4 = Student(13,40,34)
#
# print(s1.avg())
# print(s3.avg())
# print(s4.avg())
# print(Student.info())
# s1.new()
# """splitting a string """
# a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings.
# print(a)
#
# """joiniing a string"""
# a = "-".join(a)
# print(a)

"""OOP Concepts"""

class Car():

    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price

    def price_inc(self):
        self.price=int(self.price*1.15)

honda=Car('toyota',1034,1000000)
nissan=Car('nissan',8989,8853954)


print(honda.price)
honda.price_inc()
print(honda.price)


