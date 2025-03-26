# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops
# x = 0
# # define a while loop
# while(x<5):
#   print (x)
#   x=x+1
# define a for loop and use a for loop over a collection
# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#   print(i * 2)  # Print each number multiplied by 2
# use the break and continue statements
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# for d in days:
#   if (d == "Friday"):
#     break
#   print(d)
# for d in days:
#   if (d == "Thursday"):
#     continue
#   print(d)
# using the enumerate() function to get an index and an item
for a, d in enumerate(days):
  #print(f"Index: {a}, Item: {d}")
  print(a,d)