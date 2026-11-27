#Design a Python program to read an integer from the user and calculate the sum of its digits
#using while loop
# Program to find the sum of digits of a number
n = int(input("Enter an integer: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10
print("The sum of digits of", n, "is:", sum)

'''OR'''

#Using for loop
# Program to find the sum of digits of a number using for loop
n = input("Enter an integer: ")
sum = 0
for digit in n:
    sum += int(digit)
print("The sum of digits of", n, "is:", sum)

'''OR'''

#using if else
# Program to find the sum of digits of a number using if statement
n = int(input("Enter an integer: "))
if n >= 0:
    sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10
    print("The sum of digits of", n, "is:", sum)
else:
    print("Please enter a positive integer.")
