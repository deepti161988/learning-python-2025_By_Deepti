# LinkedIn Learning Python course by Joe Marini
# Example file for working with conditional statements


x, y = 10, 100

# conditional flow uses if, elif, else
if x < y:
  print("x is less than y")
elif x == y:
  print("x is equal to y")
else:
  print("x is greater than y") 
# conditional statements let you use "a if C else b"
a = 10
b = 5
c = True

result = a if c else b

print(result)  # Output: 10

c = False
result = a if c else b
print(result)  # Output: 5
