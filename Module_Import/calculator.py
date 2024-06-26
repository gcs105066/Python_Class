import add # Module
import divide
import multiply
import substract


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

