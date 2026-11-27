#Design a Python program to find the factorial of a number
n=int(input("Enter a number"))
fact=1
for f in range(1,n+1):
    fact=fact*f
print("The factorial of",n,"is",fact)
