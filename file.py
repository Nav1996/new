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




