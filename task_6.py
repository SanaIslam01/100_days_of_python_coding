# task 1

n=int(input("enter a number"))
while n>=0:
    print(n)
    n=n-1


# task 2
n=int(input("enter a number that you want to calculate the factorial"))

def factorial(n):
    f=1
    b=1
    while b<=n:
        f=f*b
        b=b+1
factorial(n)
print(factorial) 


# task 3

n=int(input("enter a number"))
def countdown(n):
   while n>=0:
    print(n)
    n=n-1
countdown(n)

