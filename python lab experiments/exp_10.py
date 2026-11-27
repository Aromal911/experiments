'''Design a Python program that reads a positive integer n from the user and prints a star pattern
of height n using the * character. The output should clearly display the pattern.'''
n = int(input("Enter the number of lines: "))
for i in range(1, n + 1): 
    for j in range(1, i + 1): 
        print("*", end=" ")
    print() 
'''             OR        '''
#Using function
def printPattern(n):
    for i in range(1,n+1): 
        for j in range(1,i+1): 
            print("*",end=" ")
        print()
n=int(input("Enter the number of lines"))
printPattern(n)
