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
n1=int(input("enter the first number: "))
n2=int(input("enter the second number: "))
print("select the operation you want to perform: ")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print("5. modulus")
choice=int(input("enter the choice: "))
if choice==1:
    print("the sum of the numbers are:",sum(n1,n2))
elif choice==2:
    print("the difference of the numbers are: ",difference(n1,n2))
elif choice==3:
    print("the product of the numbers are: ", product(n1,n2))
elif choice==4:
    print("the division of the numbers are: ",division(n1,n2))
else:
    print("the modulus of the numbers are: ", modulus(n1,n2))
