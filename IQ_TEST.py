#IQ TEST
import timeit
print("Find your IQ")
IQ=0
start = timeit.default_timer()
  
def one():
    print("1>> Which number should come next in this series? 25,24,22,19,15 ")
    print("press 1=14        2=5  \n")
    print("press 3=30        4=10  \n")
    print("press 5=12\n")
    ANS=int(input("your choice -->"))
    if ANS==4:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS 10 ")
        return 0
def two():
    print("2>>  Which one of the five is least like the other four?")
    print("press 1=Cow          2=Tiger  \n")
    print("press 3=Snake        4=Dog  \n")
    print("press 5=Bear\n")
    ANS=int(input("your choice -->"))
    if ANS==3:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS Snake")
        return 0
def three():
    print("3>> If you rearrange the letters \"BARBIT\", you would have the name of a:")
    print("press 1=Ocean        2=Country  \n")
    print("press 3=State        4=City  \n")
    print("press 5=Animal\n")
    ANS=int(input("your choice -->"))
    if ANS==5:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS Animal")
        return 0
def four():
    print("4>> Divide 30 by half and add 10. What do you get?")
    print("press 1=12           2=20  \n")
    print("press 3=70           4=30  \n")
    print("press 5=15\n")
    ANS=int(input("your choice -->"))
    if ANS==3:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS 70")
        return 0
def five():
    print("5>> Nia,  twelve years old, is three times as old as her sister. How old will Nia be when sheis twice as old as her sister?")
    print("press 1=15        2=18  \n")
    print("press 3=16        4=20  \n")
    print("press 5=21\n")
    ANS=int(input("your choice -->"))
    if ANS==3:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS 16")
        return 0
def six():
    print("6>> Which one of the five makes the best comparison? Brother is to sister as niece is to:")
    print("press 1=Mother        2=Daughter  \n")
    print("press 3=Aunt          4=Uncle  \n")
    print("press 5=Nephew\n")
    ANS=int(input("your choice -->"))
    if ANS==5:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS Nephew ")
        return 0
def seven():
    print("7>> Which one of the five letters is least like the other four? given below")
    print("press 1=N        2=F  \n")
    print("press 3=A        4=Z  \n")
    print("press 5=E\n")
    ANS=int(input("your choice -->"))
    if ANS==5:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS E")
        return 0
def eight():
    print("8>> Which one of the five makes the best comparison?Milk is to glass as letter is to:")
    print("press 1=Stamp        2=Pen  \n")
    print("press 3=Envelope     4=Book  \n")
    print("press 5=Mail\n")
    ANS=int(input("your choice -->"))
    if ANS==3:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS Envelope")
        return 0
def nine():
    print("9>> If a doctor gives you three pills and tell you to take one pill every half hour, so how long it will take to consume all pills")
    print("press 1=2 hours       2=45 min  \n")
    print("press 3=1 hour        4=30 min \n")
    print("press 5=none\n")
    ANS=int(input("your choice -->"))
    if ANS==3:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS 1 hour")
        return 0
def ten():
    print("10>> How many birthdays does the average man have?")
    print("press 1=1        2=Every year  \n")
    print("press 3=Every year except leap year \n")
    ANS=int(input("your choice -->"))
    if ANS==1:
        print("CONGRATULATIONS YOUR ANSWER IS CORRECT")
        return 13
    else:
        print(" WRONG ANSWER")
        print("CORRECT ANSWEWR IS 1")
        return 0

IQ = IQ + one()
print("\n")
IQ = IQ + two()
print("\n")
IQ = IQ + three()
print("\n")
IQ = IQ + four()
print("\n")
IQ = IQ + five()
print("\n")
IQ = IQ + six()
print("\n")
IQ = IQ + seven()
print("\n")
IQ = IQ + eight()
print("\n")
IQ = IQ + nine()
print("\n")
IQ=IQ+ten()
print("\n")
stop = timeit.default_timer()
a= stop - start
print('Time-Taken: ', a)
print("Your Intelligence is")

#bonus points
if a>=150:
    IQ=IQ+5
elif a>=100:
    IQ=IQ+10
else:
    IQ=IQ+20
    
#result
if IQ >= 130:
    print("Extremely High ")
elif IQ >=120:
    print("Very High ")
elif IQ >=110:
    print("High Average  ")
elif IQ >=90:
    print(" Average ")
elif IQ >=80:
    print("Low Average ")
elif IQ >=70:
    print("Borderline ")
else: 
    print("Extremely Low ")


    
        
