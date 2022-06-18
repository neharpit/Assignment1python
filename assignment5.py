
#Question 1
def reverse(string):
    string=string[::-1]
    return string
s=input("Enter a string",)
print("The original string is:")
print(s)
print("The reversed string is:")
print(reverse(s))


#Question 2
a=int(input("Enter the lower limit of the range:",))
b=int(input("Enter the upper limit of the range:",))
n=int(input("Enter a number:",))
for i in range(a,b+1):
    if(i%n==0):
        print(i)
    i+=1


#Question 3
a=float(input("Enter 1st side:",))
b=float(input("ENter 2nd side:",))
c=float(input("Enter 3rd side:",))
if((a+b)/2>c):
    if((a+c)/2>b):
        if((b+c)/2>c):
            print("semi perimeter=")
            s=(a+b+c)/2
            print("area of triangle according to heron's formula is")
            area=(s*(s-a)*(s-b)*(s-c))**0.5
            print(area)
else:
    print("invalid entry")



#Question 4
n=int(input("Enter the number of rows:"))
t=(n//2)+1
l=n//2
for i in range(1,t+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for q in range(1,0,-1):
    for r in range(q,0,-1):
        print("*",end="")
    print()

#Question 5
row=int(input("Enter the number of rows"))
n=0

for i in range(0,row+1):
    for j in range(i):
        if n==26:
            n=0
        else:
            pass
        y=chr(65+n)
        print(y,end="")
        n+=1
    print("")


#Question 6
a=int(input("Enter the lower limit of the range:",))
b=int(input("Enter the upper limit of the range:",))
print("The prime  numbers in this range is:")
for i in range(a,b+1):
    if i>1:
        for n in range(2,i):
            if(i%n)==0:
                break
            else:
                print(i)
    
#Question 7
for i in range(1,501):
    if(i%7==0):
        if(i%11==0):
            print(i)

#Question 8
pos=[]
neg=[]
odd=[]
even=[]
times=[]
li=[]
for i in range(10):
    num=int(input("Enter the number:"))
    li.append(num)
    if num>=0:
        pos.append(num)
    elif num<0:
        neg.append(num)
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
    if num not in times:
        times[num]=1
    else:
        times[num]+=1
print("Positive numbers are:",pos)
print("Negative numbers are:",neg)
print("Even numbers are:",even)
print("odd numbers are:",odd)
print("Number of times each number occurs in the list",times)


#Question 9
n=int(input("Number of words:"))
li=[]
for i in range(n):
    word=input("Enter the word:")
    li.append(word)
times={}
for i in li:
    if i not in times:
        times[i]=1
    else:
        times[i]+=1
print("Number of occurence:",times)