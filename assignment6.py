#Question 1
#checking whether a number is perfect or not
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
print(perfect_number(6))

#Question 2
def palindrome(n):
    if len(s)<1:
        return True
    else:
        if s[0]==s[-1]:
            return palindrome([1:-1])
        else:
            return False
a=str(input("Enter a string:"))
if(palindrome(a)==True):
    print("String is palindrome")
else:
    print("String is not a palindrome")

#Question 3 
def pascal_triangle(n):
    x=[1]
    y=[0]
    for i in range(max(n,0)):
        print(x)
        x=[1+r for 1,r in zip(x+y,y+x)]
    return n>=1
pascal_triangle(6)


#Question 4
import string

def pangram(str):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

#Question 5
n=input("Enter the string:")
l=n.split("-")
l.sort()
print("-".join(|))

#Question 6
def student_data(student_id,**kwargs):
    print(f'\nStudent ID:{student_id}')
    if 'student_name'in kwargs:
        print(f"Student Name:${krawrgs[student_name]}")
    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name:${krawrgs[student_name]}")
        print(f"\nStudent Class:${krawrgs[student_class]}")

s=input("Enter student's id:")
d=input("Enter student's name:")
g=input("Enter student's class:")
student_data(student_id="s",student_name="d")
student_data(student_id="s",student_name="d",student_class"g")


#Question 7
class Student:
    pass 
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
#Question 8

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


#Question 9 
class validity:
    def f(str):
        a=['()','{}','[]']
        while any(i in str for i in a):
            for j in a:
                str=str.replace(j,'')
                return not str
s=input("enter:")
print(s,"-","is balanced"if validity.f(s) else "is unbalanced")
