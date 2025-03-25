# LinkedIn Learning Python course by Joe Marini
# Example file for complex types


# Dictionary: a key-value data structure
my_dict = {"apple": 1, "banana": 2, "orange": 3}

# dictionaries are accessed via keys by different methods as belows
print(my_dict["banana"])
print(my_dict.get("orange"))
# you can also set dictionary data by creating a new key
my_dict["strawberry"] = ["small","medium", "large"]
print(my_dict)
# Trying to access a nonexistent key will produce an error
try:
  print(my_dict["grape"])  # This will raise a KeyError
except KeyError:
  print("Error: Key 'grape' does not exist in the dictionary.") 
# To avoid this, you can use the "in" operator to see if a key exists
if "banana" in my_dict:
  print("banana is in my dictionary")
print("banana" in my_dict)
print("guava" in my_dict)
# You can retrieve all of the keys and values from a dictionary
keys = my_dict.keys()
values = my_dict.values()
print(keys)
print(values)

# You can also iterate over all the items in a dictionary
