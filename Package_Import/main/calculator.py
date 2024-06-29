#calulator is package
#indivitual file is module
import sys # module 
import os

print(sys.path)

#['/Users/praveenkumar/Desktop/Python/main', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages']

current_path=os.path.dirname(__file__)

print(current_path)

#/Users/praveenkumar/Desktop/Python/main

join_with_calculator=os.path.join(current_path,'..')

print(join_with_calculator)

#/Users/praveenkumar/Desktop/Python/main/..

sys.path.append(join_with_calculator)


#print(sys.path.append(join_with_calculator))

#sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
#'/Users/praveenkumar/Desktop/Python

#sys.path.append('/Users/praveenkumar/Desktop/Python')

print(sys.path)



from calculation import add 
from calculation import divide
from calculation import multiply
from calculation import substract


def calculator(num1,num2,operator):
    num3=0

    if operator =='Addition':
       num3= add.addition(num1,num2)

    elif  operator =='divide':
        num3= divide.division(num1,num2)

    elif  operator =='multiply':
        num3=multiply.multiplication(num1,num2)

    else :
        num3=substract.substraction(num1,num2)

    return num3

num1=int(input("Give the first number "))
num2=int(input("Give the second number "))
operation=input("Which operation you want to do ")
print(calculator(num1,num2,operation))

print("My program is running fine ")

