# # LinkedIn Learning Python course by Joe Marini
# # # Example file for complex types

# # # Sequences: Lists and Tuples
# # # These are -- surprise -- sequences of values
my_list = [1, 2, 3, "apple", True]
# # print(my_list)
# # print(type(my_list))

# # # Tuple Example
my_tuple = (1, 2, 3, "banana", False)
# # print(my_tuple)
# # print(type(my_tuple)) 

# # # to access a member of a sequence type, use []
# # print(my_list[2])
# # print(my_list[-2])
# # my_list[1]=20
# # print(my_list)

# # # add a list to another list
another_list = [11, 12, 13, "banana", False]
# # new_list = my_list + another_list
# # print(new_list)

# # use slices to get parts of a sequence
str="this is a bag"
# print(str[1:10:1])

# # you can use slices to reverse a sequence
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[::-1]
# print(sliced_list)    # Output: [5, 4, 3, 2, 1]

# # Tuples are like lists, but they are immutable
# my_tuple = (1, "hello", 3.14)
# print(my_tuple[0])
# print(my_tuple[-1])
# # Sets are also sequences, but they contain unique values
my_set = {1,2,3,4,5}
print(my_set)
# # Set, however, can not be indexed like lists or tuples
##print(my_set[1])    #this will cause an error as set is not indexed

# # Test for membership
print(6 in my_list)
print(3 in my_tuple)
print(3 in my_set)
print(19 in another_list)

