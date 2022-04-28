# Exercise 1 - Print the numbers from 1 to 10 on the screen. Use a list to store the numbers.

list1 = []

for i in range(0, 10):
    list1.append(i+1)

print("Exercise 1 answer:")
print(list1)

# Exercise 2 - Create a list of 5 objects and print it on the screen

list2 = []

for i in range(0, 5):
    a = str(i+1)
    list2.append("object" + a)

print("Exercise 2 answer:")
print(list2)

# Exercise 3 - Create two strings and concatenate them into a third string

str1 = "First String"
str2 = "Second String"
str3 = str1 + " " + str2
print("Exercise 3 answer:")
print(str3)

# Exercise 4 - Create a tuple with the following elements: 1, 2, 2, 3, 4, 4, 4, 5 and then use the count function of
# tuple object to check how many times the number 4 appears in the tuple

tuple1 = (1, 2, 2, 3, 4, 4, 4, 5)

print("Exercise 4 answer: \n" + str(tuple1.count(4)))

# Exercise 5 - Create an empty dictionary and print it to the screen

dct1 = {}
print("Exercise 5 answer:")
print(dct1)

# Exercise 6 - Create a dictionary with 3 keys and 3 values and print it on the screen

for i in range(0, 3):
    a = "key" + str(i+1)
    b = "value" + str(i+1)
    dct1[a] = b

print("Exercise 6 answer:")
print(dct1)

# Exercise 7 - Add one more element to the dictionary created in the previous exercise and print it on the screen

dct1["newValue"] = "New Key"

print("Exercise 7 answer:")
print(dct1)

# Exercise 8 - Create a dictionary with 3 keys and 3 values. One of the values must be a list of 2 numeric elements.
# Print the dictionary on the screen.

dct2 = {"Value1": "KeyOne", "Value2": [10, 20], "Value3": "KeyThree"}

print("Exercise 8 answer:")
print(dct2)

# Exercise 9 - Create a list of 4 elements. The first element must be a string,
# the second a 2-element tuple, the third a dictionary with 2 keys and 2 values and
# the fourth element a value of type float.
# Print the list on the screen.

list3 = ["The first element is a string",
         ("The Second Element", "Is a 2-element tuple"),
         {"The third is a dictionary": "With Two Keys", " and Two Values": "The Fourth Element is a float"},
         3.1415]

print("Exercise 9 answer:")
print(list3)

# Exercise 10 - Consider the string below. Print on the screen only characters from position 1 to 18.
phrase = 'Data Scientist is the best professional of the 21st century'

print("Exercise 10 answer:")
print(phrase[:18])
