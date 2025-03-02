#sys is the package is used to read the values in command line arguments.
import sys
def sum(num1,num2):
    add=num1+num2
    return add
def difference(num1,num2):
    sub=num1-num2
    return sub
def product(num1,num2):
    mul=num1*num2
    return mul
def division(num1,num2):
    div=num1/num2
    return div
def modulus(num1,num2):
    mod=num1%num2
    return mod
n1=int(sys.argv[1])              #command line arguments
operation=sys.argv[2]
n2=int(sys.argv[3])
if operation=="add":
    output=sum(n1,n2)
    print(output)
if operation=="sub":
    output=difference(n1,n2)
    print(output)
if operation=="mul":
    output=product(n1,n2)
    print(output)
if operation=="div":
    output=division(n1,n2)
    print(output)
if operation=="mod":
    output=modulus(n1,n2)
    print(output)
