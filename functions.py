#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
# A function can return data as a result



x="Hey user"

def test():
    print("Python is awesome" + x)
test()
#Basic function writtern and calling:
#To call a function, use the function name followed by parenthesis:
def GreetMe(name):
    print("Good Morning"+name)

def Orbcomm():
    print("Orbcomm is enterprise project")
Orbcomm()

def UX():
    print("I want to print UX in the front end")
UX()




# Creating a function using methods and variables
#function with variables examples


#List
def variable_num():
    A=[1,2,3,4,5]
    print(A[0],[1])
variable_num()

def variable_string():
    B=["Nithish", "Sam"]
    print(B[1])
variable_string()

def variable_add():
    A=10
    B=22
    print(A+B)
variable_add()

def variable_sub():
    A=56
    B=22
    print(A+B)
variable_sub()

## Function creating with the arguments

def variable(fname, lname):
    print("User credentials" + fname)
    variable(fname="Chiti", lastname = "The bot")





##Variable using the for loop concept

def loop():
    for x in range(1,11):
        print(x)
loop()



##Tuple

##If else conditions function
def Test_case(Positive):
    a=100
    if a>4:
        print("Test case is executed")
    else:
        print("Test case got failed")
Test_case("Positive scenario")






def AddIntegers(a,b):
    return a+b
print(AddIntegers(2,3))

def Add_multiply(a,b):
    return a*b
print(Add_multiply(3,4))

def Add_subtraction(a,b):
    return a-b
print(Add_subtraction(4,5))

def Variable():
    Test:list =["Samsung",2,3,4,5]
    print(Test[0][1])
    A=4
    if A>2:
        print("Test pass")
    else:
        print("Test fail")

Variable()

#Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
def Name(Firstname, Lastname):
    print(Firstname+"K",Lastname+"K")

Name("Nithish","Test")
Name("Krishna","Krishna")



def Regression():
    a=100
    if a>4:
        print("A value is greater than 4")
    else:
        print("A is less than 4")
Regression()


#Arbitary Arguments (If you don't know how many arguments to pass in the function * keyword is used before the arg name

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

##Keyword Arguments is passed key=value syntax

def my_func(child1, child2, child3):
    print("The youngest child"+child2)

my_func(child1="Nithi", child2="Nithish", child3="Kumar")

#If the number of keyword arguments is unknown, add a double ** before the parameter name:

def myfun(**key):
    print(key["fname"])
myfun(lastname= "Krishna", fname="Moor")


class Game:
    num=90

    def getdata(self):
        print("Good Morning")

Obj=Game()
Obj.getdata()
print(Obj.num)


def add():
    print("Addition:")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a+b)
add()

def sub():
    print("Subtraction:")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a-b)
sub()

def multiply():
    print("Multiply:")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a*b)
multiply()

def mutlip():
    a=int(input("Enter a:"))
    b=int(input("Haa B:"))
    print(a+b)
mutlip()


def division():
    print("Division:")
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a/b)
division()

def painter(msg):
    print("Message:",msg)
painter("test")

def painter(msg):
    print("Message:", msg)
painter("I need to paint my house")


def findevenorodd(a):
    if a%2==0:
        print("Even")
    else:
        print("Odd")
b=int(input("Enter a:"))
findevenorodd(b)

def userpassorfail(a):
    print("Pass status")
    if a>35:
        print("User is pass")
    else:
        print("User is fail")
b=int(input("Enter a value:"))
userpassorfail(b)

def printtrange(l1,l2):
    for i in range(l1,l2):
        print(i)
a=int(input("Enter a value"))
b=int(input("Enter b value"))
printtrange(a,b)

















