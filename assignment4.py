#Question 1 :
x=int(input("Enter Marks:",))
if(x<25):
    print("F")
elif(x>=25 and x<45):
    print("E")
elif(x>=45 and x<50):
    print("D"):
elif(x>=50 and x<60):
    print("C")
elif(x>=60 and x<80):
    print("B")
elif(x>=80):
    print("A")
else:
    print("Not applicable")

#Questin 2:
y=int(input("Enter the year:"))
if y%4==0:
    print("This is a ldap year")
elif y%100==0:
    print("This year is not a leap year")
elif y%400:
    print("This is a leap year")
else:
    print("This year is not leap year")


#Question 3:
import random
for i in range(10):
    number_1=random.randint(1,10)
    number_2=random.randint(1,10)
    print(f"question{i+1}:",end="")
    user_output=int(input(f"{number_1}X{number_2}="))
    if user_output==(number_1*number_2):
        print("right")
    else:
        print(f"The answer is wrong.The right answer is {number_1*number_2}")


#Question 4:
x=200
for candies in range(x):
    if candies%5==2:
        if candies%6==3:
            if candies%7==2:
                print(candies,"candies are there in the bowl")
                break 


