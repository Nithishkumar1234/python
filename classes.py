##

##Classes are user defined blueprint or prototype
##Example Calculator (Sum, multiply, sub, division) all the operations in one class or different methods in one class.
##Class will operate with variables and methods.
##In class variables having two types (Class variables, Instance variables)

#Instance variables will change when creating every obj but class variables is fixed one dones not change
#Self keyword is mandatory to call the variables in methods
#__init__ used to create a constructor


class AI:
    M=100 ##Class variables defined after the class.

    def __init__(self,name):  #Constructor method (It will be called automatically when object is created)
        self.firstname=name

    def summation(self):
        return self.firstname

obj=AI("a")
print(obj.summation())

obj=AI("Usability")
print(obj.summation())



class nithish:

    def Logintest(self):
        a=100
        b=30
        if a>b:
            print("Awesome")
        else:
            print("failure")
obj=nithish()
print(obj.Logintest())


class Calculator: #class name - calculator
    num=100 ##Variables

    def __init__(self): ##Constructor - No need to call the constructor to call the method.
        print("Print the output")

    def getdata(self):
        print("Iam printing the object output")

obj=Calculator()
obj.getdata()
print(obj.num)


class Nithish:
    num=35

    def __init__(self):
        print("Yahoo!")

    def List(self):
        A=[1,"ASD",3,4,5,6,7]
        print(A[0],[1])

obj=Nithish()
obj.List()
print(obj.num)


#Using constructor

class test():

    def __init__(self, fname, lastname):
        self.fname=fname
        self.lastname=lastname

p=test("Nithish", "Kumar")
print(p.fname)
print(p.lastname)


p=test("Yashwanth", "Kumar")
print(p.fname)
print(p.lastname)











