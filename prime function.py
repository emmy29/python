
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True



n=input("enter a number =")
for x in range(2,int(n)):
    if prime(x):
        print(x," is prime")
    else:
        print(x," is not prime")
        
