#working with tupples
a=('name',"Adarsh","MCA")#tupple is immutable
print(a)
print(len(a))
print(a[:2])
print(a[:1])
print('name' in a)

b=1234,'abc',1.2
print(b)
print(type(b))

#unpacking of tupple
x, y, z=b
print(x)
print(y)
print(z)
#packing of tupple
x=123456789
y="adarsh"
z=1234.56789
m=x,y,z

print(m)
print(type(m))



