#Q1 Average of three numbers entered by user 
n1=int(input("Please Enter First Number"))
n2=int(input("Please Enter Second Number"))
n3=int(input("Please Enter Third Number"))
avg=(n1+n2+n3)/3
print("The average of 3 Numbers is:",avg)

#Q2 Computing Person's income tax 
gross_income=float(input("Enter your gross income:"))
number_of_dependents=float(input("Enter no of Dependents"))
std_deduction=10000
deduction2=int(number_of_dependents*3000)
tax_income=int(gross_income)-int(std_deduction)-int(number_of_dependents*3000)
tax=(tax_income*20)/100
if(tax<0):
 print("invalid input")
if(tax>0):
 print("tax:",tax)

#Q3 Storing different data type values in a list
SID=int(input("Enter your SID:"))
Name=input("Enter your Name:")
Gender=input("Enter your Gender:")
Course=input("Enter your Course Name:")
CGPA=float(input("Enter your CGPA:"))
Student=[SID,Name,Gender,Course,CGPA]
print("student:",Student)

#Q4 Entering marks of 5 Students
m1=int(input("Marks of 1st student:"))
m2=int(input("Marks of 2nd student:"))
m3=int(input("Marks of 3rd stident:"))
m4=int(input("Marks of 4th student:"))
m5=int(input("Marks of 5th student:"))
Sortedmarks=[m1,m2,m3,m4,m5]
print(Sortedmarks)

#Q5 a. Removing 4th element
List_of_colors=['RED','Green','White','Black','Pink','Yellow']
print("List of colors before removing:",List_of_colors)
List_of_colors.remove('Black')
print(List_of_colors)


#Q5 b. Replacing Black and Pink with Purple
List_of_colors=['Red','Green','White','Black','Pink','Yellow']
print("List  of colors before replacing:",List_of_colors)
List_of_colors[3:5]=['Purple']
print("your list after replacing black and pink color with purple:",List_of_colors)