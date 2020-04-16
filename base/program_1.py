#!/usr/bin/python

# First you have to include the python url as in line 1
# Second add permisions to the file with chmod +x file.py

# Program:
print("Hello!")

#Global Variable
x = 8

def sum ():
  global x 
  y = 8
  x += y

sum()

print(x)