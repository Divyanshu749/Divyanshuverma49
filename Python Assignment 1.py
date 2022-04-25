23
78
# Question 1 Soln :
number_1 = int(input("Enter first number: "))    #taking input from user as an integer
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

#Average = (sum of all numbers)/Total number of elements
Average = (number_1 + number_2 + number_3)/3

print("Entered values: ", number_1 ,",", number_2 ,",", number_3)
print("Average of the given values: ", Average)
        
#Question 2 :
Gross_income = float(input("Enter your Gross income(in $): "))

Dependents_in_family = int(input("Enter number of dependents in your family: "))

Standard_deduction = 10000     # to be charged on all taxpayers (in $)

tax_rate = 0.2     #20% tax rate charged on all taxpayers

deductionn_per_dependent = 3000   # (in $)

Taxable_income = Gross_income - Standard_deduction - (deductionn_per_dependent*Dependents_in_family)

Tax = Taxable_income*tax_rate

print("Taxable income: ", Taxable_income)
print("Tax:", Tax)

#Question 3 Soln :
seconds = int(input("Enter the total number of seconds: "))

#For minutes
minutes = seconds//60  # floor divisio operato is used.

#For minute _seconds
minute_seconds = seconds%60  # Modulus operator is used.

print("Entered", seconds,"seconds", "=" , minutes,  "minutes" , minute_seconds,"seconds")

#Question 4 :
num1 = 25            #integer.
num2 = int('25')     #string convert it to integer. 
num3 = int(25.0)     #float value converted to integer.


Addition = num1 + num2 + num3

Str_Addition=str(Addition)        #Convert the desired result in string.

print("Addition: ", Str_Addition)
print(type(Str_Addition))

#Question 5 :
import math            #First import math modules to use sine and cosine functions

i = 0
while i <= 345:        #While loop is used to make a loop of each 15degree angles
    sine = math.sin(math.radians(i))    #using sine and cosine functions from math module
    cosine = math.cos(math.radians(i))
    
    print("sin(",i,"):", round(sine, 4),",", "Cos(",i,"):", round(cosine, 4))
    i+= 15