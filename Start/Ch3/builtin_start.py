# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#
mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
# length_of_string = len(mystring)
# length_of_list = len(mynumbers)
# print("Length of the string is :", length_of_string)
# print("Length of the list is :", length_of_list)
# # the max() and min() functions will find the largest and smallest value in a sequence
# maximum_number = max(mynumbers)
# print("Maximum number:", maximum_number)  # Output: 20
# minimum_number = min(mynumbers)
# print("Minimum number:", minimum_number)

# the str() function will return a string version of an object
# prefix = "result: "
# result = 5
# print(prefix + str(result))

# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops 
# for i in range(5,15,1):
#   print(i)
for i in range(1,len(mystring),2):
  print(mystring[i])


# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10
print(f"{greeting} You are in a queue, {count} people are ahead of you!")