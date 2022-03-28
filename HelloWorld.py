from math import gcd, sqrt, trunc
from random import randint, uniform
from re import M


print("BTMN")
#end = 
print("A", end=" <3 ")
print("B", end=" \nhihi")

#sep =
print("A","B","C",sep=" --- ")

""" This is
command
"""
#---------------------------------------
#variable
#-number or word
#-no space, no (+,-,*,:,...)
#no start by number

a=5
b=10
print("a = ", a)
#Gan bien rut gon
#phai co gia tri bien cuoi
x=y=z=2
x,y,z = 4,5,6
a,b = b,a

#Dia chi o nho, id()
print("Id of a: ", id(a))
c=5
d=5
print("Id of c: ", id(c))
print("Id of d: ", id(d))

#Random
#Random int in [a,b]
randint(15,20)
#Random R number in [a,b]
uniform(15,20)

#tinh phan nguyen
trunc(x)
#lam tron (len) n chu so
round(5.964455,4)
#v==0.3
v=.3
#-------------------------------
#min, max
min(a,b,c)
max(a,b,c)
#gia tri tuyet doi
abs(a)
sqrt(a)

#uoc chung lon nhat
gcd(a,b)
#boi chung nho nhat
bcnn = a*b // gcd(a,b)

#-----------------------------------------
#Cau truc re nhanh
#if - else
#if (a==True) = if a
#if 1 <a <b <5

print('Yes') if True else print('No')

#------------------------------------------
# Multi rows
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    if fruit == 'apple':
        print('I eat it in the morning')
# One row
[print('I eat it in the morning') for fruit in fruits if fruit == 'apple']

#continue: dung trong vong lap, cac lenh sau continue se ko hoat dong, ma se quay lai vong lap
for x in 1,2,3,4,5:
    if x%2==0:
        continue
    print("x la so le")

#break: khi dung break chuong trinh se thoat khoi vong lap
for x in 1,2,3,4,5:
    if x==4:
        break
    print(x)

#tim UCLN
a = int(input())
b = int(input())



