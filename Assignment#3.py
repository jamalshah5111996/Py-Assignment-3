#!/usr/bin/env python
# coding: utf-8

# In[9]:


#TASK1:
print("\nTASK1:\n");
Poem= "Twinkle, twinkle, little star,\n\t How I wonder what you are! \n\t\t Up above the world so high,\n\t\t Like a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are!\n"
print(Poem);
#TASK2:
print("\nTASK2:\n");
from platform import python_version
print("Python-Version=",python_version());
#TASK3:
print("\nTASK3:\n");
import datetime
now = datetime.datetime.now()
print ("Current date and time :",now.strftime("%Y-%m-%d %H:%M:%S"))
#TASK4:
print("TASK4:\n");
radius = int(input("Write the radius of the circle:"))
pi = 3.146
area = pi*radius*radius
print("Area of the Circle:",area,"square units")
#TASK5:
print("\nTASK5:\n");
first_name = input("Write your first Name:")
last_name = input("Write your Last Name:")
print(last_name,first_name)
#TASK6:
print("\nTASK6:\n");
a=int(input("\nwrite the value of a:"))
b=int(input("write the value of b:"))
print("sum of a+b=",a+b)
#TASK7:
print("\nTASK7:\n");
eng = int(input("Write your English Marks out of 100:"));
isl = int(input("Write your Islamiat Marks out of 100:"));
math = int(input("Write your Mathematics Marks out of 100:"));
phy =int(input("Write your Physics Marks out of 100:"));
chem =int(input("Write your Chemistry Marks out of 100:"));
total =500;
obt_total = eng + isl + math+ phy + chem;

percent = obt_total/total *100;
percentage =round(percent);

if obt_total <=500 and obt_total >=0:
    print("Total Obtained Marks:",obt_total,"/",total);

if percentage <=100 and percentage >=0:
    print("Your Percentage is:",percentage,"%");
else:
    print("Invalid Marks!");

if percentage <= 100 and percentage >=80:
    print("Grade: A+")
elif percentage <= 79 and percentage >=70:
    print("Grade: A")
elif percentage <= 69 and percentage >=60:
    print("Grade: B")
elif percentage <= 59 and percentage >=50:
    print("Grade: C")
elif percentage <= 49 and percentage >=40:
    print("Grade: D")
elif percentage <= 39 and percentage >=0:
    print("Failed")
else:
    print("Review Your Marks.");

# TASK8:
print("\nTASK8:\n");
number=int(input("Write a number to check it is Even or Odd:"))
if number %2 ==0:
    print("it is even number")
else:
    print("it is odd number")
# TASK9:
print("\nTASK9:\n");
cars= ["Tesla","Toyota","Honda","Chevorlet","Range rover","Cadillac"];
leng= len(cars);
print("Total Cars:",leng);
# TASK10:
print("\nTASK10:\n");
nums=[10,20,100,200,500,300,800,900];
Summ =sum(nums);
print("Sum of all numbers in the list is:",Summ)
# TASK11:
print("\nTASK11:\n");
list=[80,404,556,60,87,1000,20,800,600];
largNo=max(list)
print("Largest Number in the list is:",largNo)
# TASK12:
print("\nTASK12:\n");
e = [1, 2, 3, 4, 5, 6, 8, 7, 8, 9, 10, 11]
for y in e:
    if y < 5:
        print(y);

