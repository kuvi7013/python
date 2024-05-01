#printing the string
print("Hello World!")


print("=====syntax - indentation =====")

#indentation in python is more important. unlike other languages, indent defines the block in python
if 3 < 5:
	print("3 is less than 5")
	print("indent is used")

#wrong indent
if 3 < 5:
        print("3 is less than 5")
        #	print("wrong indent is used")


#multi line commands
#python will ignore the string whne not assigned to variables

"""
This is a comment
with multiple lines
and python will ignore this as it is 
not assigned to any variable
"""

print("=====VARIABLES=====")

#variables

#A variable is created the moment you first assign a value to it.

#Python has no command for declaring a variable.

x = 5
y = "John"
print(x)
print(y)

#If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print("x,y,z = ",x,y,z)

#You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

#String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'


#Variable names are case-sensitive.

x = 4
X = "Sally"


print("x, X =", x, X)
#A will not overwrite a


print("=====variable name rules=====")
print("""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
""")

print("=====Python Variables - Assign Multiple Values=====")
#Python allows you to assign values to multiple variables in one line:
print("a,b,c=1,2,3")
a,b,c = 1,2,3
print("a,b,c=",a,b,c)

print("a,b,c = 'hello'")
a = b = c = 'hello'
print("a,b,c=",a,b,c)

print("If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.")

print("sample_list=[1,2,3]")
sample_list=[11,22,33]
a,b,c = sample_list
print("a,b,c=",a,b,c)



print("=====String cancatenation=====")
a = "this "
b = "is a "
c = "Good day"
print(a+b+c)
#note we have adde the space after each string, else it will be joint without space

print("=====Global variables=====")
"""
Variables that are created outside of a function (as in all of the examples above) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

x = "global defined outside x"

def func():
	x = "local defined inside func"
	print(x)

func()

print(x)


"""
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Also, use the global keyword if you want to change a global variable inside a function.

"""

x = "global defined ouside func"

def func():
	global x
	x = "Global variable modified inside function"
	print(x)

func()
print(x)



