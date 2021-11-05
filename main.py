# first_name = "Jaca"
# last_name = "Nemo"
# full_name = first_name + " " + last_name
# #print(type(name))
# print("Hello "+full_name)

# age = 188
# age += 1
# print("Your age is: " +str(age))
# print(type(age))

# height = 13.13
# print("You are this tall: " +str(height) + " CM" )
# print(type(height))

# human = True
# print("You are human: " +str(human))
# print(type(human))

#multiple assignment = assign multipule varibles at the same time in one line of code

# name = "Jaca"
# age = 33
# attractive = False

# name, age, attractive = "Jaca", 33, False
#
# print(name)
# print(age)
# print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30
#
# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

#string methods

# name = "Jaca"
#
# print(len(name)) #print length of string
# print(name.find("c")) #find index of char
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit()) #boolean on if str is a digit or not
# print(name.isalpha()) #boolean on if alphabetical char or not
# print(name.count("a")) #count chars in str
# print(name.replace("a", "o"))
# print(name*3) #not technically a method

#type casting = converting data type of a value to different data type

# x = 1 #int
# y = 2.0 #float
# z = "3" #str
#
# x = str("X is "+str(x))
# y = str("Y is "+str(y))
# z = str("Z is "+str(z))
#
# print(x)
# print(y)
# print(z)
#
# print(type(x))
# print(type(y))
# print(type(z))

#user input

# name = input("What is your name?: ")
# age = int(input("What is your age?: "))
# height = float(input("What is your height?: "))
#
# print("Hello, "+name+".")
# print("You are "+str(age)+" years old.")
# print("You are "+str(height)+" inches tall.")

#maths
# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
#
#
# print(round(pi))
# print(math.ceil(pi)) #ceil as in ceiling - rounds up
# print(math.floor(pi)) #rounds down
# print(abs(pi)) #absolute value (how far a num is away from zero)
# print(pow(pi,2)) #pow = power. Raises a number to the value of
# print(math.sqrt(pi)) #square root
# print(max(x,y,z))
# print(min(x,y,z))

#slicing - create a substring by extracting elements from another string
#indexing[] or slice()
#[start:stop:step]

# name = "Jaca Nemo"
#
# first_name = name[:4]
# last_name = name[5:]
# funky_name = name[::]
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7,-4)
#
# print(website1[slice])
# print(website2[slice])

#if - elif - else

# age = int(input("How old are you?: "))
#
# if age == 100:
#     print("Congrats! You're hanging in there.")
# elif age >= 18:
#     print("You are an adult.")
# elif age < 0:
#     print("Whu?")
# else:
#     print("You are a child.")

#logical operators (and, or, not)

# temp = int(input("What is the temperature outside?: "))
#
# if not(temp >= 0 and temp <= 30):
#     print("Bad temperature!")
#     print("Stay inside!")
# elif not(temp < 0 or temp > 30):
#     print("The temperature is nice today!")
#     print("Go outside!")

#while loop

# name = ""
#
# while len(name) == 0:
#     name = input("Enter your name: ")
#
# print("Hello "+name)

# import time
# #for loop = a statement that will execute it's block of code a limited amount of times
# #while loop = unlimited
# #for loop - limited
#
# for i in range(10):
#     print(i + 1)
#
# for i in range(1, 10+1,2):
#     print(i)
#
# for i in "Jaca Nemo":
#     print(i)
#
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

#nested loops = inner loop

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end ="")
#     print()

#Loop control statements = change a loop execution from it's normal sequence
#break = terminate loop entirely
#continue = skips to next iteration of loop
#pass = does nothing, acts as placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phonenumber = "123-456-7890"
#
# for i in phonenumber:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)

#lists
#
# food = ["pizza", "chicken", "chocolate", "yummy"]
#
# food[0] = "sushi"
#
# #food.append("ice cream")#add a value
# #food.remove("sushi") #remove a value
# #food.pop() #removes last element
# #food.insert(0, "cake")
# #food.sort()
# food.clear()

#print(food[0])

# for x in food:
#     print(x)

#2D Lists = a list of lists
#
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "chicken"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food[2][1])

#tuple = collection which is ordered and unchangeable used to group together related data

# student = ("Jaca", 31, "male")
# print(student.count("Jaca"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Jaca" in student:
#     print("Jaca is here.")

#set = collection which is unordered, unindexed. No duplicate values.

# utensils = {"fork", "spoon", "knife", "spork"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("napkin")
# utensils.clear()
# dishes.update(utensils)
# dinnertable = utensils.union(dishes)
#
# for x in dinnertable:
#     print(x)

# print(dishes.difference(utensils))
# print(utensils.intersection(dishes))

#dictionary = changable unordered collection of unique keey:value pairs
#Fast because they use hashing, allow access to value quickly

# capitals = {'USA':'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}
#
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# capitals.clear()

# print(capitals['Russia'])
# print(capitals.get('Germany'))
# print(capitals.keys()) #prints only keys and not values
# print(capitals.values()) #prints only values and not keys
# print(capitals.items()) #prints everything

# for key,value in capitals.items():
#     print(key, value)

# index operator [] = gives access to a sequence's element
#str,list,tuples

# name = "jaca Nemo!"
#
# # if(name[0].islower()):
# #     name = name.capitalize()
#
# firstname = name[:4].upper()
# lastname = name[5:].lower()
# lastchar = name[-1]
#
# print(firstname)
# print(lastname)
# print(lastchar)

#function = a bloc of code executed only when it is called.

# def hello(firstname, secondname, age):
#     print("Hello "+firstname+" "+secondname)
#     print("You are lucky number "+str(age)+" winner.")
#     print("Have a nice day!")
#
# # my_name = "Stu"
# # hello(my_name)
# #
# # hello("Jaca")
# # hello("Dude")
# hello("Chris", "Jaden", 13)

#return statement = Functions send Python values/objects back to caller.
                #   These values/objects are known as the fuction's return value

# def multiply(num1, num2):
#    return num1 * num2
#
#
# x = multiply(6,8)
# print(x)

#keyword arguments

# def hello(first,middle,last):
#    print("Hello "+first+" "+middle+" "+last)
#
# hello(last="III", first="Jaca", middle="Nemo")

#nested function calls = function calls inside other function calls

# num = input("Enter a while positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

#scope = the region that a variable is recognized
#A variable is only available from inside the region it is created
#A global and locally scoped sersions of a variable can be created

# name = "Jaca" #global scope = available inside & outside functions
#
# def display_name():
#     name = "Nemo" #local scope = available only inside this function
#     print(name)
# display_name()
# print(name)

#LEGB rule = Local, Enclosing, Global, Built-in

#*args = parameter that will pack all arguments into a tuple
#useful so a function can accept a varying amount of arguments

# def add(*narf):
#     sum = 0
#     narf = list(narf)
#     narf[0] = 0
#     for i in narf:
#         sum += i
#     return sum
#
# print(add(1,2,3,4,5,6))

# **kwargs = parameter that will pack all arguments into a dictionary
#useful so that a function can accept a varying amount of keyword arguments

#*args = varying amount of positional arguments into tuples
#**kwargs = varying amount of keyword arguments into dictionary

# def hello(**names):
#     #print("Hello "+kwargs['first']+" "+kwargs['last'])
#     print("Hello", end=" ")
#     for key,value in names.items():
#         print(value, end=" ")
#
# hello(title="Queen",first="Jaca", middle="Narf", last="Nemo")

# str.format() = optional method gives user more control when displaying output

# animal = "cow"
# item = "moon"
#
# #print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,"moon"))
# print("The {0} jumped over the {0}".format(animal,"moon")) #positional argument
# print("The {item} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(item, animal))

# name = "Jaca"
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you.".format(name)) #padding
# print("Hello, my name is {:<10}. Nice to meet you.".format(name)) #left aline
# print("Hello, my name is {:>10}. Nice to meet you.".format(name)) #right aline
# print("Hello, my name is {:^10}. Nice to meet you.".format(name)) #center aline

# number = 1000
#
# print("The number pi is {:.2f}".format(number)) #f is for floating point number
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number)) #binary
# print("The number is {:o}".format(number)) #octal number
# print("The number is {:x}".format(number)) #hexadecimal
# print("The number is {:X}".format(number)) #hexadecimal
# print("The number is {:e}".format(number)) #scientific notation
# print("The number is {:E}".format(number)) #scientific notation