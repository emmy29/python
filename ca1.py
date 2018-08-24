#assume an employee of an organisation using paython data structure store the details of employee and display using looping techniques
fixed_info=("Name--->Adarsh","Emp_id--->1170","Dept--->Data_analysis","joining_date--->24-08-2018","nationality--->Indian")#this information is stored using tuple becuase it is fixed and doesn't change
for i in fixed_info:
    print(i)
var_info={"age":22,"position":"supervisor","salary":25000}#this info stored using dictionary and it can be changed 
for k,v in var_info.items():
    print(k,"--->",v)
skills=["hadoop","rapid-miner","No-sql"]#here list is used because new skills can be learned
print("skills --->")
for i in skills:
    print(i)

