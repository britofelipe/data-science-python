# Exercise 1 - Create a structure that asks the user for the day of the week. If the day is equal to Sunday or
# equal to Saturday, print on the screen "You need to rest", otherwise print on the screen "You need to work!"

print("Exercise 1 answer:")
dayOfTheWeek = input("What day is it today? ")

if (dayOfTheWeek == "Saturday") or (dayOfTheWeek == "saturday") or (dayOfTheWeek == "Sunday") or (dayOfTheWeek == "sunday"):
    print("You need to rest.")
else:
    print("You need to work!")

# Exercise 2 - Create a list of 5 fruits and check if the 'Strawberry' fruit is part of the list

print("Exercise 2 answer:")
fruitsToBuy = ["Orange", "Strawberry", "Apple", "Banana", "Lemon"]
isStrawberry = 0
for item in fruitsToBuy:
    if item == "Strawberry":
        isStrawberry = 1

if isStrawberry == 1:
    print("Strawberry is on the list.")
else:
    print("Strawberry isn't on the list.")

# Exercise 3 - Create a 4-element tuple, multiply each element of the tuple by 2 and store the results in a
# list

print("Exercise 3 answer:")
tp = (1, 2, 3, 4)
list1 = []
for item in tp:
    list1.append(item*2)
print(list1)

# Exercise 4 - Create a sequence of even numbers between 100 and 150 and print it on the screen

print("Exercise 4 answer:")
list2 = []

for i in range(100, 151, 2):
    list2.append(i)
print(list2)

# Exercise 5 - Create a variable called temperature and assign the value 40. As long as temperature is greater than 35,
# print the temperatures on the screen

print("Exercise 5 answer:")
temperature = 40
while temperature > 35:
    print("The temperature is", temperature, "degrees")
    temperature -= 1

# Exercise 6 - Create a variable called counter = 0. While counter is less than 100, print the values on the screen,
# but when the value 23 is found, stop the program execution

print("Exercise 6 answer:")
counter = 0
while counter < 100:
    print(counter)
    if counter == 23:
        break
    counter += 1

# Exercise 7 - Create an empty list and a variable with value 4. As long as the variable's value is less than or equal to 20,
# add to the list, only the even values and print the list

print("Exercise 7 answer:")
list3 = []
variable = 4
while variable <= 20:
    list3.append(variable)
    variable += 1
print(list3)

# Exercise 8 - Transform the result of this range function into a list: range(5, 45, 2)

print("Exercise 8 answer:")
nums = range(5, 45, 2)
print(list(nums))

# Exercise 9 - Correct the errors in the code below and run the program. Hint: there are 3 errors.

print("Exercise 9 answer:")
temperature = float(input('What is the temperature? '))
if temperature > 30:
    print('Wear light clothes.')
else:
    print('Look for your coats.')

# Exercise 10 - Write a program that counts how many times the letter "r" appears in the sentence below. Use a placeholder in
# your print instruction

# “It is better, much better, to be content with reality; if she is not as bright as dreams, she at least has the
# advantage of existing.” (Machado de Assis)

print("Exercise 10 answer:")
phrase = "It is better, much better, to be content with reality; if it is not as bright as dreams, it at least has the advantage of existing."
count = 0

for i in phrase:
    if i == "r":
        count += 1

print("The letter 'r' appears %i times" %(count))
