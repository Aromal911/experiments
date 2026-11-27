#To write a program to reverse a 3 digit number
# Reverse a three-digit number using mathematical operations
num = int(input("Enter a three-digit number: "))
# Method 1: Using mathematical operations
rev = (num % 10) * 100 + ((num // 10) % 10) * 10 + (num // 100)
print("Reversed number:", rev)
