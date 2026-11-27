'''
Design a Python program to read a positive integer n from the user and generate the Fibonacci
series up to n terms. The program should display the series in order, separated by spaces.
'''
#using if else
count=int(input("Enter the number of terms"))
if count==1:
    print("0")
elif count==2:
    print("0")
    print("1")
else:
    prev1=0
    prev2=1
    print(prev1)
    print(prev2)
    for i in range(count-2):
        next=prev1+prev2
        print(next)
        prev1=prev2
        prev2=next
        next=prev1+prev2
'''                 OR       '''
#Using for loop
# Program to print Fibonacci series up to n terms
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b
'''OR'''
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

