#scope and user defined function
n1=10
def square(x):
    n2=n1**2
    return n2
print(n1)
print(square(3))
n1=20
print(square(3))



n1=20
def square(x):
    global n1
    n2=n1**2

    return n2
print(square(3))
n1=20
print(square(3))
