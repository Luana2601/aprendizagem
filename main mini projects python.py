# Function to print Hello World
print ('Hello World')

# Variable of different types
first_name = 'Luana' # string
age = '39' # integer

print('Hello, my name is', first_name, 'and I am', age, 'years old')

#variable declaration
num1 = 3.3
num2 =  1.1
result = num1 / num2
print('The result of the division is', result)  

#function input
first_name = input('Please enter your name:') # string
age = int(input('Please enter your age:'))  #integer

print('Hello, {}! You are {} years old.'.format(first_name, age))
print('Hello,', first_name, 'You are', age, 'years old.')
print(f'Hello, {first_name}! You are {age} years old.')


#ask the user to enter two numbers
#calculator
#print the result of the sum, subtraction, division, multiplication and exponentiation

num1 = float(input('Please enter the first number:'))
num2 = float(input('Please enter the second number:')) 

sum = num1 + num2
subtraction = num1 - num2
division = num1 / num2
multiplication = num1 * num2
exponentiation = num1 ** num2


print(f'Sum: {sum}')
print(f'Subtraction: {subtraction}')
print(f'Division: {division}')
print(f'Multiplication: {multiplication}')
print(f'Exponentiation: {exponentiation}')


#list
#remove
#for loop


fruits = ['Apple', 'Grape', 'Orange', 'Banana', 'Cherry']

print(fruits)

fruits = ['Orange', 'Apple', 'Mango', 'Banana', 'Cherry']


print(f'The first fruit is: {fruits[0]}')
print(f'The last fruit is: {fruits[4]}')
print(f'The last fruit is: {fruits[-2]}')

removed_fruit = fruits.pop(0)
print(f'The removed fruit is: {removed_fruit}')

for fruit in fruits:
    print('I like to eat', fruit) 


#for loop

for i in range(1, 11):
    print(i)

#for loop /  fruit and vegetables
fruits = ['Orange', 'Apple', 'Mango', 'Banana', 'Cherry']
vegetables = ['Carrot', 'Potato', 'Tomato', 'Cucumber', 'Onion']

for fruit in fruits:
  for vegetable in vegetables:
    print('I like to eat', fruit, 'and', vegetable)


#while loop 
i = 2
while i <= 7:
  print(i)
  i += 1

# loop / break, continue
print('loop with break:')
for i in range(1, 50):
  if i > 10:
    break
  print(i)

print('loop with continue:')
for i in range(1, 50):
  if i == 10:
    continue
  print(i)

# counter fruits
fruits = ["Orrange","Aplle", "grape", "banana", "Aplle", "Aplle", "cherry"]
counter = 0

for fruit in fruits:
  if fruit == "Aplle":
    counter += 1

print("Number of Aplles in the liste: ", counter)

#if else
i = int(input("Enter a number: " ))

if i >10:
    print("The number is greater than 10")
else:
    print("The number is less than or equal to 10")



#if elif else
age = int(input("Enter your age: "))

if age < 18:
   print("You are an children.")  
elif age >= 18 and age < 65:
   print("You are an adult.")
else: 
   print("You are an senior.")

#if else stock
stock = ['corolla', 'prius', 'hrv', 'civic']   
search_car = input('Enter car to search: ')

if search_car in stock:
    print('The car is available in stock')
else: 
    print('The car is not available in stock')

#while loop / break
while True:
  fruit = input("Enter a fruit: ")  
  if fruit.lower() == "mango":
    break

print("Congratulations, you got the fruit right!")


 #for loop even or odd
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))

for i in numbers:
  if i % 2 == 0:
    print(f'The number {i} is even')
  else:
    print(f'The number {i} is odd')



#tuple
city = ('São Paulo', 'Rio de Janeiro', 'Salvador', 'Belo Horizonte', 'Fortaleza', 'Curitiba', 'Recife', 'Porto Alegre', 'Manaus', 'Belém')
city_user = input("Enter a city: ")
if city_user in city:
    print("City found")
else:
    print("City not found")

#coutry_capital 
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires"
}
Country_user = input("Enter the name of the country: ")

if Country_user in capitals:
    print(f"The capital of {Country_user} is {capitals[Country_user]}")  
else :
    print("Sorry, the capital of that country is not in our database")


#sets
friends1 = {"Mirella", "João", "Bruna", "Thalita", "Edu"}
friends2 = {"Edu", "Jalva", "Adriana", "Mirella"}

#result = friends1.intersection(friends2)
#result = friends1.union(friends2)
result = friends1.difference(friends2)
print(result)

#def return
def square(number):
    return number ** 2

num= int(input("Enter a number: "))
print(f'The square of {num} is {square(num)}')

#exponentiation
def potence(base,exponent=2):  
    return base**exponent

user_number = int(input("Enter the number: "))
user_exponent = input('Enter the exponent (default 2): ')

if user_exponent:
    print(f'The result is: {potence(user_number, int(user_exponent))}')
else:
    print(f'The result is: {potence(user_number)}')


#factorial
def factorial(n):
   if n == 0 or n == 1:
      return 1
   else:
      return n * factorial(n - 1)

user_number = int(input("Enter a number: "))
print(f'The factorial of {user_number} is{factorial(user_number)}')

#two functions
def tobend(num):  
  return num * 2

def square(num):  
  return tobend(num) ** 2

user_number = int(input("Enter a number: "))
print(f"Square of the to bend number {user_number} is: {square(user_number)} ",)


#lambda function
#def cubo(num):
 #   return num**3
cubo = lambda num: num ** 3

user_number = int(input('Enter a number: '))
print(f'The cube of {user_number} is {cubo(user_number)}')

#lambda function multiplies two numbers

#def multiply(num1, num2):
   # return num1 * num2

multiply = lambda num1, num2: num1 * num2
user_number1 = int(input("Enter a number: "))
user_number2 = int(input("Enter a number: "))
print (f'The multiplication of {user_number1} and {user_number2} is {multiply(user_number1, user_number2)}')


#lambda if / else
#def even_or_odd(number):  
#  if number % 2 == 0:
#    return "Even"
#  else:  
#    return "Odd"

even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

user_number = int(input("Enter a number: "))
print(f'The number {user_number} is {even_or_odd(user_number)}.')

#lambda for loop
numbers = [1, 2, 3, 4, 5]
square = lambda num: num ** 2

result = []
for i in numbers:
  result.append(square(i))
  print(f'The square of the {numbers} is {result}')



