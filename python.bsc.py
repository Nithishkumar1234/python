#Python is a popular programming language.
#Python can be used on a server to create web applications.
#Python is a popular programming language. It was created by 'Guido van Rossum', and released in 1991.

#It is used for:
#1.web development (server-side),2.Software development, 3.Maths, 4. System scripting

#What can Python do?
#Python can be used on a server to create web applications.
#Python can be used alongside software to create workflows.
#Python can connect to database systems. It can also read and modify files.
#Python can be used to handle big data and perform complex mathematics.
#Python can be used for rapid prototyping, or for production-ready software development.

#Comments can be used to explain Python code.
#Comments can be used to make the code more readable.
#Comments can be used to prevent execution when testing code.

##To check python version in command line >>>>'python --version'

#To check the Python version of the editor, you can find it by importing the sys module

import sys
print(sys.version)

print("I am learning Automation")
print("Success")
print(3)
print("test")

#To get output we should use command 'print' in python.
print ("Hello User")
print("How are you?","Who are you>?")
print("Nithish ", 3)
print('Hey')
print("Hey")
print(4)
print(type(5.0)) ## Output <class 'float'>
print("I want to learn python programming effectively")

print("Happy Thursday")
print(5,"Hey you!!")
print("Hey user")



## Variable - Variables are containers for storing data values.
##Variable names are case-sensitive.
#Integer, Float, boolean, string
A=3,"Test",5.0
print(A)
a="Variable"
print(a)
b='Text'
print(b)
c=45.7
print(type(a),type(b),type(c))
d=bool(True)
print(d)
e=bool(False)
print(e)
Mass=1
mass=1
MASS=1
print(Mass,MASS,mass)

User ="Software professional", 4, 6.0
print(User)
print([0])





## If you want to specify the data type of variable, this can be done with casting.
A= str("User") ##A will print 5
B= int(34) ##B will print 34
C= float(3) ##C will print 3.0
D= bool("e")
print(A,B,C,D)


##Arthimetic operators - Addition, Multiplication, Subtraction, Division, Floor Division, Modulus and Exponential
print(5+4) #Addition
print(2*5) #Multiply
print(10-4) #Sub
print(2/2) #Divison
print(2//4) #Floor div - It will print the next bigger value
print(2**3) #Exponential
print(5%3) #Modulus


#Multi type variable names for readability
# Camel case - 1st letter will be small case and remaining words in capital
my_Variable = "Nithish"
#Pascal case - Each word starts with capital letter
My_Variable = "Krishnamoorthi"
#Snake case - Each word is separated by an underscore character:
my_variable_c= 4

print(my_Variable)
print(My_Variable)
print(my_variable_c)

##You can get the data type of variable with the type() function.
print(type(A))
print(type(b))
print(type(C))

Str ="hello world"
print(Str)

JS=[1,2,"Nithish", "Holiday"] #List
print(JS[0], [1])


b,c, d = 2, 3, "great" ##Variable
print(b,c,d)

U="hello world test"
print(U.upper())

#if different datatype is passed in variable  we need to pass the below args
print("{} {}".format(3, b))
print("{} {}".format("value c is", c))
print("{} {}". format("value d output is",c))
print("{} {}".format("value d is ", b))
print("{} {}".format("value d is",d))

print ("{} {}".format('value m is', d))



#"""If same data type is passed in the variable we can use + (concatenating) """"
# concatenating refers to the process of joining two or more strings (text values) together into a single string.
G="test"
T="user 1"
print(G+ "Output function","sd" + T+ "pass")

N="Hello user how have you been?"
K="Hello"
print(N, K)



#Data types - Data type will define the variable
#--->Numeric, string, list, tuple & Dictionary

#List can be to store multiple items in the single variable
#Indexing - accessing individual elements in sequences such as strings, lists, tuples, etc., using their position (index)
# For Extracting specific data ,Looping through sequences ,Slicing subsequences
values=[1, 2, "Hello", 10]

#if we want to get last number we need to call [-1]
print(values[0]) # Output - 1
print(values[-1]) # Output - [-1] index is used to print the last value
print(values[1:3]) # Output - 2 , "Hello" it will give output from index 1 and -1 ( 3rd index will not give as an output)


Data = [1,2,3,4,5,6,7,8,9,0]
print(Data[0])
print(Data[3])
print(Data[8])
print(Data[1:5]) #The output will be [1,2,3,4,5]
print(Data[-1]) # The output will be last value


#we can inject a value also inbetween the list using this command values.insert
values.insert(4,"hello world")
print(values)

values.insert(5,"Hey user")
print(values)

Data.insert(3,"Mytest")
print(Data)

values.insert(2,"Strings")
print(values)

#If we want to add new variable in the list at last we can use command called append
values.append("python")
print(values)

Data.append(5)
print(Data)

values.append("Nithish Kumar Krishnamoothi")
print(values)

#To update the values
values[2]= "UAT testing"
print(values)

values[3]="user"
print(values)

values[3]="Test user preference"
print(values)

Data[0]="Tech jays"
print(Data)

Data[1]="hey"
print(Data)


#To delete the values in the list
del values[1]
print(values)

del values[2]
print(values)

del Data[1]
print(Data)

values.append("I want to print python as  output")
print(values)

del Data[0]
print(Data)

#Tuple is immutable it is same as List but can't update the data once the variable is declared
## Tuple is used curve bracket which List used square bracket

tests=(1,2,3,4,5)
print(tests[1],[2],[4])
print(tests[1:3])
print(tests[1:4])
###############################################################################################


#Dictonary - data structure that stores key-value pairs.
#A dictionary is a collection which is ordered, changeable and do not allow duplicates.
#(unordered, mutable, and allows fast lookups, additions, and deletions)


fig={"Hello":3, 5:"HYE"}
print(fig["Hello"])

dic = {1:"test", "a":4}
print(dic[1])
print(dic["a"])

dic.update({1:"hello", "a":5, 5:"hello"})
print(dic)

rem={"rem 1":"Front wheel", 2:"Rear wheel"}
print(rem["rem 1"], [2])


dct={}
for i in range(4):
    dct[i]=i+6
print(dct)

for x in "test":
    print(x)
for y in "usability":
    print(y)
for z in range(1,4):
    print(z*1)

#Equals: a == b , Not Equals: a != b , Less than: a < b , Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b



#If else conditions
Greeting= "Good Morning"
if Greeting == "something":
    print("conditions matches")
else:
    print("conditions do not match")

Nithish ="Active Person"
if Nithish !="Active person":
    print("Pass")
else:
    print("Fail")

a=6
if a>4:
    print("Im greater than you")
else:
    print("Im lesser than you")
print(a)

b=6
if b<=5:
    print("Won")
else:
    print("Lose")
print(b)

#Match expression in python
#Instead of writing many if else statements, we can use the match statement.
Day = 1
match Day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Looking forward for your response")

Nithish = 1
match Nithish:
    case 1:
        print("Nithish working as QA Engineer")
    case 2:
        print("Like and comment")


#Create an empty dictionary to call dynamically
test={}
test["Firstname"]= "NithishK"
test["Lastname"]="Kumar"
test["Email ID"]="nithishkumar.@gmail.com"
print(test)
print(test["Email ID"])

test.update({"Firstname":"Krishna", "Lastname":"Moorthy"})
print(test)

test.update({"Email ID":"nithishkrishnamoorthi08@gmail.com"})
print(test)


#for loop
#Control flow statement used to iterate over a sequence
#Use cases - Automate the repetitive task , to calculate, to iterate range of numbers using range()
#To make the task like searching, sorting , filtering the data

fruits = ['apple', 'banana', 'cherry'] #In list method
for fruit in fruits:
    print(fruit)

Boys = ['Nithish', 'Yash', 'Kishore',]
for Boy in Boys:
    print(Boys)

Apple=['vitamin A', 'Vitamin B']
for apple in Apple:
    print(Apple)

#Using the loop in string
for x in "banana":
    print(x)

#The output will take 0 to 4 and it will be multiplied
for i in range (5):
    print(i*2)

for i in range(1,11):
    print(i,"x2",i*2)

for x in range(4):
    print(x+2)

for z in range(1,11):
    print(z,"X2",z*3)

techjays=["Nithish","Ashvanth"]
for techjay in techjays:
    print(techjay)

for c in range(1,10,2):
    print(c)

for b in "Use me":
    print(b)
###Break statement in loops
fruitss = ["apple", "banana", "cherry"]
for x in fruitss:
  print(x)
  if x == "banana":
    break

it=4
while it>3:
    print(it)
    it=it-1
ir=5
while ir>1:
    if ir !=3:
        print(ir)
    ir=ir-1

iy=10
while iy>2:
    if iy==4:
        break
    print(iy)
    iy=iy-1
print("While loop is completed")






































