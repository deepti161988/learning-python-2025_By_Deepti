# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def first_function():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)
# first_function()
# function that takes parameters
# def second_function(greet):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greet, name)
# second_function("good morning ")
# second_function("How r u ")
# function that returns a value
# def cube(x):
#   return(x*x*x)
# result=cube(3)
# print (result)
# function with default value for an parameter
# def param_function(greet="Hello"):
#     name = input("What is your name? ")
#     print(greet, name)
# param_function("Good morning")
# param_function("How are you")
# param_function()  # This will use the default value "Hello"

# function with variable number of parameters
def param_many_function(greet="Hello" , name="Sir/Maam"):
    #name = input("What is your name? ")
    print(greet, name)

param_many_function("Good morning")
param_many_function("How are you")
param_many_function()  # This will use the default value "Hello"