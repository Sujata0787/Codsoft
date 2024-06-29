def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y==0:
        return "cannot divide by zero"
    else :
        return x/y
print("Select an operation")
print("1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.division")

choice=int(input("Enter your choice :)"))
if (choice in [1,2,3,4]) :
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))

    if(choice==1) :
        print("Result for your addition is :",add(a,b))
    elif(choice==2) :
        print("Result fpor your substraction  is :",substract(a,b))
    elif(choice==3) :
        print("Result for your multiplication  is :",multiply(a,b))
    elif(choice==4) :
        print("Result for your division  is :",division(a,b))

else :
    print("Enter valid option")
    
      