'''Design a Python program to read a positive integer n from the user and calculate the sum of the
first n natural numbers. The program should display the sum with a clear message.'''
n = int(input("Enter a positive integer: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of the first", n, "natural numbers is:", sum)
