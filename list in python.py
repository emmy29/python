#creating a list of numbers#
easy_as=[1,2,3]
print(easy_as)
#creating a list of strings#
strlist=['adarsh', 'amal', 'jaja', 'chanda']
print(strlist)
empty=[]
print(empty)
mixed=[1,2,'adarsh','jaja']
print(mixed)
#list start from 0 index#
print(mixed[2])

#appending list#
mixed.append('chanda')
print(mixed)

#you can also slice the list
print(mixed[:3])#slicing the list upto 3 index but index is excluded

print(mixed[1:-1])#slicing the list starting the list from 1 index untill -1 index

#nested lists #
nested_list=[mixed,easy_as]
print(nested_list)

#printing individual list from a nested list#
print(nested_list[0])
print(nested_list[1])


#accesssing eleements of nested list#

print(nested_list[0][3])#the first no after list name is for the sub list and 2nd no is for a particular element in sublist

