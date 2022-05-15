# Exercise 1 - Create a function that prints the sequence of even numbers between 1 and 20 (the function does not
# receive a parameter) and then make a call to the function to list the numbers
import string

print("Exercise 1 answer:")


def evenNumbers():
    list_numbers = []
    for i in range(2, 21, 2):
        list_numbers.append(i)
    print(list_numbers)


evenNumbers()

# Exercise 2 - Create a function that takes a string as an argument and returns the same string in capital letters.
# Make a call to the function, passing a string as a parameter

print("Exercise 2 answer:")


def capitalLetters(text):
    print(text.upper())
    return


capitalLetters(input("Enter your string: "))

# Exercise 3 - Create a function that takes as a parameter a list of 4 elements, adds 2 elements to the list and
# print the list

print("Exercise 3 answer:")


def addElements(array):
    array.append("Item 5")
    array.append("Item 6")
    print(array)
    return


listOfElements = ["Item 1", "Item 2", "Item 3", "Item 4"]
addElements(listOfElements)

# Exercise 4 - Create a function that takes a formal argument and a possible list of elements. make two calls
# to the function, with only 1 element and in the second call with 4 elements

print("Exercise 4 answer:")


def testVarTuple(arg1, *others):
    print("The first argument is", arg1)
    for item in others:
        print("You also passed %s as an argument" % (item))


testVarTuple(10)
testVarTuple(20, 30, "Bicycle")

# Exercise 5 - Create an anonymous function and assign its return to a variable called sum. The expression will receive
# 2 numbers as a parameter and return their sum

print("Exercise 5 answer:")

total_sum = lambda arg1, arg2: arg1 + arg2
print("The sum is:", total_sum(5, 10))

# Exercise 6 - Run the code below and make sure you understand the difference between global and local variable

print("Exercise 6 answer:")

total = 0


def sumNumbers(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function the total is: ", total)
    return total


sumNumbers(10, 20)
print("Outside the function the total is:", total)

# Exercise 7 - Below you will find a list with temperatures in degrees Celsius
# Create an anonymous function that converts each temperature to Fahrenheit
# Tip: to be able to perform this exercise, you must create your lambda function, inside a function
# (which will be studied in the next chapter). This allows you to apply your function to each element in the list
# How to find the math formula that converts from Celsius to Fahrenheit? Search!!!
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda args: (float(9) / 5 * args + 32), Celsius)
print("Exercise 7 answer:")
print(list(Fahrenheit))

# Exercise 8
# Create a dictionary and list all dictionary methods and attributes

print("Exercise 8 answer:")
dictio = {"value1": "key1",
          "value2": "key2",
          "value3": "key3"}
print(dir(dictio))

# Exercise 9
# Below you can find the Pandas import, one of the main Python packages for data analysis.
# Carefully review all available methods. One of them you will use in the next exercise.

print("Exercise 9 answer:")
import pandas as pd
dir(pd)

# ************* Challenge ************* (search the Python documentation)
# Exercise 10 - Create a function that takes the file below as an argument and returns a descriptive statistical summary
# of the file. Tip, use Pandas and one of its methods, describe()
# File: "binary.csv"

from IPython.display import display

file_name = "binary.csv"
binary_df = pd.read_csv(file_name)
display(binary_df.describe())
display(binary_df.describe())
