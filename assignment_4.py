# Assignment 4
# Name: Divyanshu Verma
# SID: 21107109
# Branch: Mechanical
# Question 1
a=int(input("enter your marks:"))
if(a<25):
    print("F")
elif(a>=25 and a<=45):
    print("E")
elif(a>45 and a<=50):
    print("D")
elif(a>50 and a<=60):
    print("C")
elif(a>60 and a<=80):
    print("B")
elif(a>80 and a<=100):
    print("A")

# Question 2

year = int(input('Enter year:'))
if(year%100 == 0 and year % 400 == 0 and year%4==0):
        print("Leap year")
else:
    print("Not a leap year")
#Question 3
import random

for i in range(1, 11):
    a =random.randint(0, 9)
    b =random.randint(0, 9)
    ans = int(input(f'Question {i}:{a}x{b}='))
    if ans == a * b:
        print('Right!')
    else:
        print('Wrong. The correct answer is', a * b)
#Question 4
for i in range(200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("The number of pieces in the bowl are:", i)