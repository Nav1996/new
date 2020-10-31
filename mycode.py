import pandas as pd
import random
from math import sqrt
emp_details={'employee':{'dave':{'ID':'001','salary':'3000','designation':'team lead'},'ava':{'ID':'003','salary':'9000','designation':'team member'}}}
print(emp_details['employee'])
my_dict={'ava':'001','adam':'003'}
for x,y in my_dict.items():
    print(x,y)
my_dict['ava']='004'
my_dict['chris']='005'
print(my_dict)
my_dict.pop('ava')
print(my_dict)

print(my_dict.popitem())

df=pd.DataFrame(emp_details['employee'])
print(df)

print(133//4)

val1=100
val3=100

if val1==val3:
    print('values are equal')
elif val1>val3:
    print('val1 is greater')
else:
    print('val3 is greater')

print(val3>0 and val1==0)


list1=[1,3,4,5]
list3=[1,4,5,65,3]
y=list1 is list3
num =0
while num<9:
    print('number',num)
    num+=1

print('good bye')

n=30
to_be_guessed=int(n*random.random())+1
guess=0
while guess!=to_be_guessed:
    guess=int(input('new number '))
    if guess>to_be_guessed:
        print('number is too large')
    elif guess<to_be_guessed:
        print('number is too small')
    elif guess==to_be_guessed:
        print('congragulations you made it')
    else:
        print('ur giving up')


fruits=['mango','banana','grapes']

for fruit in fruits:
    print('current fruit',fruit)

print('thats all')

num = int(input('enter a number :'))
factorial=1

if num<0:
    print('enter a positive number')
elif num==1:
    print('factorial =1')
else:
    for i in range(1,num+1):
        factorial=factorial*i

print(factorial)


num=int(input("enter four digit print :"))
returnCard=0;
balance=int(random.random()*100000)+1
if num<1000:
    print('Entered numbeer is not four digit')

else:
    while returnCard==0:
        print('1.check balance')
        print('2.Make a withdrawal')
        print('3.pay in')
        print('4.Return card')
        select=int(input('select ur option ::  '))


        if select==4:
            returnCard=1
            print('Thank you for banking with us')
        elif select==1:
            print('ur balance is :',balance)
        elif select==2:
            wiAmount=int(input('Enter the amount'))
            if balance>wiAmount:

                balance-=wiAmount
                print('payment succsess;ur current balance is  ',balance)
            else:
                print('balance is not enough')
        elif select==3:
            inamount=int(input('Enter amount  :'))
            balance+=inamount
            print('ur current balance is  ',balance)

n=int(input("Maximum number  : "))

for a in range(1,n+1):
    for b in range(a,n):
        c_sqrt= a**2+b**2
        c= int(sqrt(c_sqrt))
        if((c_sqrt-c**2)==0):
            print(a,b,c)

def pattern(n):

    k=n*2-2
    for i in range(n,-1,-1):
        for j in range(0,k):
            print(end=" ")
        k=k+1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\n")


pattern(5)







