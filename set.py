num={1,2,3}
print(num)
print(type(num))
num1={'m','k','r'}
print(num1)
print(type(num1))
num2={9,8,7,6,5,4,3,2,1}
print(num2)
print(type(num2))

empty_set=set()
set_from_list=set([1,2,1,4,3])
print(set_from_list)
basket={"apple","orange","apple","pear","orange","banana"}
print(basket)
print(len(basket))
print("orange" in basket)
print("mango" in basket)
for fruit in basket:
    print(fruit,end='/')
    

a=set("mississippi")
print(a)
a.add('r')
print(a)
a.remove('s')
print(a)
a.discard('a')#same as remove except no error
print(a)

a.pop()
print(a)
a.pop()
print(a)
a.clear()
print(a)




b=set("adarshThakur")
c=set("emmyRajput")
print(b)
print(c)
print(b-c)#set difference
print(c-b)#set difference
print(b|c)#union
print(b&c)#intersection
print(b^c)#symmetric difference b-c|c-b









