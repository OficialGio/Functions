'''
@author: amayamunoz
'''
from distutils.command.check import check

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by 
calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.
def subtraction(num1, num2):
    subtractionOfTwoNumbers = num1 - num2
    return subtractionOfTwoNumbers

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def problem(num1):
    equation = ((num1 / 2) * 77) + 1000
    return equation

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def X(num1, num2):
    check = num1 == num2
    return check
if (check == True):
    print("True")
else:
    print("False")
    
#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def Y(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return num1
    else:
        return num2
    
#5) Define a function that takes in two words and returns a string that contains both words combined.
str1 = "Hello "
str2 = "World"
def words(str1, str2):
    combinedWord = str1 + str2
    return combinedWord

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def three(num1, num2, num3):
    if num1 == num2 or num1== num3:
        check = "True"
    else:
        check = "False"
        return check
#7) Define a function that prints your name.
def name(Gio):
    name = "Gio"
    return name

#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."
favoriteColor = "Red"
def color(color1):
    if color1 == favoriteColor:
        answer = ("That's my favorite color!")
    else:
        answer = ("That's not my favorite color. Try again")
    return answer

#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def finalnumber(num1):
    while num1 > 0:
        num1 -= 1
        
'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.
def division(num1, num2):
    quotient = num1/ num2
    return quotient
