#creating a dictionary #
empty={}#creating an empty dictionary
print(type(empty))#finding type of dictionary
print(empty==dict())#checking if a variable is of dictionary or not

a=dict(one=1,two=2,three=3)
print(type(a))
b={"one":1,"two":2,"three":3}
print(a==b)

about={"name":'adarsh',"age":22,"class":'MCA',"Birth_place":'himachal',"contect":8628911655}
print(about)
#using a list as dictionary element
about={"name":'adarsh',"age":22,"class":'MCA',"Birth_place":'himachal',"alias":["emmy","anku"],"contect":8628911655}
print(about['name'])#here name is a key and adarsh is the value
print(about['age'])
print(about['Birth_place'])

about['class']="grandmaster"#modifying an key in the dictionary
print(about)


#different ways to access a list
a=about.get("name",[])
print(a)
b=len(a)
print(b)

#delete a key value from dictionary
del about["Birth_place"]
print(about)

#remove and return about["name"] or default value if not in the map
about.pop("name")
print(about)

#remove and return an arbitrary key value pair

about.popitem()#remove the last element from dictionary
print(about)

print(about.keys())#to print keys
print(about.values())#to print values
print(about.items())#to print the pair of key and values

print(len(about.keys()))
print(('age',22) in about.items())#member in function
#to print all values or keys in the dictionary
for keys in about.keys():
    print(keys)
    
for values in about.values():
    print(values)

print(len(about))

s=about.copy()
print(s)
t=about
print(t)
