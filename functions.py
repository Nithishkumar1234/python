#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
# A function can return data as a result


def GreetMe(name):
    print("Good Morning"+name)

GreetMe("Nithish") #To call a function, use the function name followed by parenthesis:

def Testcase(Positive):
    a=100
    if a>4:
        print("Test case is executed")
    else:
        print("Test case got failed")
Testcase("Positive scenario")

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









