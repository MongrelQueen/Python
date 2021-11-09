#prints the words "Hello World"
'''
print('Hello World')
"""
This is a comment
This is also a comment
This is yet another comment
"""
'''
userAge = 0

userAge, userName = 40, "Chris"
#case sensitive username != userName
# = is called the assignment operator. It assigns the value on the rt side to the variable on the lft
'''
x = 5
y = 10
y = x
print ('x = ',x)
print ('y = ',y)
'''
#Basic operators +.-,*,/,//,%,** -> addition, subtraction, multiplication, division, floor division, modulus, exponent

x, y = 5, 2

x + y
x - y
x * y
x / y
x // y #Floor division rounds down the answer to the nearest whole number
x % y
x ** y

'''
+= shorthand that combines the assignment sign w/the addition operator
-= shorthand that combines the assignment sign w/the subtraction operator
*= shorthand that combines the assignment sign w/the multiplication operator
'''


#data types - int, float, string
#type casting - changing data type
#advanced data types - the list, tuple, dictionary

#userAge = '40' <- str    userAge = 40 <- int

#brand ='Apple'
#exchangeRate = 1.235235245
#message ='The price of this %s laptop is %d USD and the exchange rate is %.2f USD to 1 EUR' %(brand, 1299, exchangeRate)
#print(message)
#%s -> string formatter
#%d -> integer formatter
#%f -> float formatter

#message ='The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235235245)
#print(message)


mess1 = '{0} is easier than {1}'.format('Python','Java')
mess2 = '{1} is easier than {0}'.format('Python','Java')
mess3 = '{:10.2f} and {:d}'.format(1.234234234, 12)
mess4 = '{}'.format(1.234234234)

#print(mess1)
#print(mess2)
#print(mess3)
#print(mess4)

#Lists = collection of data which are normally related

#listName = [initial values]
#userAge = [21,22,23,24,25]
'''
userAge[0] = 21
userAge[1] = 22
userAge[-1] = 25
userAge[-2] = 24
'''
#Can also declare a list w/out assigning any initial values
#listName =[]
#use the append() method to add items to list
#userAge2 = userAge[2:4] = you are assigning items w/index 2 to index 4(-1) from the list userAge to userAge2
#userAge2 = [23,24] (the item at the start index is always included, item at the end is always excluded)
#notation 2:4 is a slice
#stepper
#userAge3 = userAge[1:5:2]
#userAge3 = [22,24]
'''
to add items, append() function
userAge.append(99) -> adds the value 99 to the end of the list
userAge = [21, 22, 23, 24, 25, 99]
'''
'''
myList = [1, 2, 3, 4, 5, "Hello"]

print(myList)
print(myList[2])
print(myList[-1])
myList2 = myList[1:5]
print(myList2)
myList[1] = 20
print(myList)
myList.append("How are you")
print(myList)
del myList[5]
print(myList)
'''
#tuples -> are just like lists but you cannot modify their calues. Their initial values are the values that will stay for the rest of the program.
#to declare a tuple you write tupleName = (initial values)
'''
months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
print(months)
print(months[-1])
'''
#dictionary is a collection of related data PAIRS.
#to declare a dicitionary you write dictionaryName = {dictionary key : data}

#myDictionary = {"Peter":38, "John":51, "Alex":13, "Alvin":"Not Available"}

#you can also declare a dictionay using the dict() method.

#userNameAndAge = dict(Peter = 38, John = 51, Alex = 13, Alvin = "Not Available")

#print(userNameAndAge["John"])

'''
to modify items in a dictionary -> dictionaryName[dictionary key of item to be modified] = new data
'''
#userNameAndAge["John"] = 21
#print(userNameAndAge)
#print(myDictionary)

#blank dictionary -> dictionaryName = {} -> to add items dictionaryName[dictionary key] = data

#userNameAndAge["Joe"] = 40
#print(userNameAndAge)
#del userNameAndAge["Alex"] #delete an item
#print(userNameAndAge)
'''
myDict = {"One":1.35, 2.5:"Two Point Five", 3:"+", 7.9:2}
print(myDict)
print(myDict["One"])
print(myDict[7.9])
myDict[2.5] = "Two and a Half"
print(myDict)
myDict["New item"] = "Hi. I'm new."
print(myDict)
del myDict["One"]
print(myDict)
'''
'''
userInput = input('Enter 1 or 2: ')

if userInput == "1":
    print ("Hello World")
    print ("How are you?")
elif userInput == "2":
    print ("Python Rocks!")
    print ("I love Python")
else:
    print ("You did not enter a valid number.")
'''
#the syntax for looping through an iterable ->
#for a in iterable:
    #print(a)
'''
pets = ['cats', 'dogs', 'rabbits', 'hamsters', 'horses', 'birds']
for myPets in pets:
    print(myPets)
for index, myPets in enumerate(pets):
    print(index, myPets)

age = {'Ayla': 1, 'Beau':1, 'Chris':40, 'Jaden':30}
for i in age:
    print(i)
for i in age:
    print("Name = %s, Age = %d" %(i, age[i]))
for i, j in age.items():
    print("Name = %s, Age = %d" %(i,j))
'''
#message = 'Hello'
#for i in message:
#    print(i)
#for ind, i in enumerate (message):
#    print(ind, i)
'''
for i in range(5):
    print(i)
for i in range(3,10):
    print(i)
for i in range(4, 10, 2):
    print(i)
'''
#counter = 5
#while counter >0:
#    print("Counter = ", counter)
#    counter -= 1
'''
j = 0
for i in range(5):
    j += 2
    print ('i = ', i, ', j = ', j)
    if j == 6:
        break
'''

#j = 0
#for i in range(5):
#    j += 2
#    print('\ni = ', i, ', j = ', j)
#    if j == 6:
#        continue
#    print ('I will be skipped over if j = 6')
'''
try:
    answer = 12/0
    print(answer)
except:
    print("An error occurred")
'''
'''
try:
    userInput1 = int(input("Please enter a number: "))
    userInput2 = int(input("Please enter another number: "))
    answer = userInput1/userInput2
    print("The answer is: ", answer)
    myFile = open("missing.txt",'r')
except ValueError:
    print("Error: You did not enter a number")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except Exception as e:
    print("Unknown error: ", e)
'''
#If you want to display the message, use the 'as' keyword after the error type ->
#except ValueError as e:
#   print (e)
'''
print("Hello World")
newString = "Hello World".replace("World","Universe")
print(newString)
'''
#defining your own function ->
#def functionName(list of parameters):
#    code detailing what the function should do
#    return [expression]
'''
def checkIfPrime (numberToCheck):
    for x in range(2, numberToCheck): #a for loop to divide the parameter numberToCheck by all numbers from 2 to numberToCheck - 1 to determine if the remainder is zreo
        if (numberToCheck%x == 0):
            return False
    return True
'''
'''
message1 = "Global Variable"

def myFunction():
    print("\nINSIDE THE FUNCTION")
   #Global variables are accessible inside a function
    print(message1)
   #Declaring a local variable
    message2 = "Local Variable"
    print(message2)
'''
#Calling the function
#Note that myFunction() has no parameters.
#Hence, when we call this function,
#we use a pair of empty parentheses.
'''
myFunction()
print("\nOUTSIDE THE FUNCTION")

#Global variables are accessible outside function
print(message1)
#Local variables are NOT accessible outside function.
print(message2)
'''
'''
message1 = "Global Variable (shares name w/local variable)"

def myFunction():
    message1 = "Local Variable(shares name w/global variable)"
    print("\nINSIDE THE FUNCTION")
    print(message1)

#Calling the function
myFunction()

print("\nOUTSIDE THE FUNCTION")
print(message1)
'''


