#1
'''For taking length of string
First take input of string'''
string = "Python is a case sensitive language"

#len() is used for taking length of given string.
print("A) Length of the given string: ",len(string),"\n")

# This is for giving output string in reverse order.
print("B) Reverse of the given string is :")
print(string[::-1],"\n")

#slicing the string.
new_string = string[10:26]
print("C) New sliced string is: ","\n", new_string,"\n")

#replace a string using replace fun. in string slicing,
Replaced_string= string.replace('a case sensitive' , 'object oriented')
print("D) String after replacing: ", "\n" ,Replaced_string ,"\n")

#Finding the index of "a" in the input string.
print("E) Index of substring 'a' is:", string.find("a"),"\n")

#Printing the string without white spaces using replace in string.
print("F) Sting without white spaces: ","\n",string.replace(" ", ""))

#2
Name = "Divyanshu Verma"
SID = "21107109"
CGPA = "9.9"
department_name = "Mechanical Engineering"

print("Hey,",Name, "Here!\nMy SID is", SID,"\nI am from", department_name, "department and my CGPA is", CGPA )

#3
# Use of Bitwise Operators.
a = 56
b = 10

# Use of Bitwise AND(&) operator.
print("A. a & b =", a & b)

# Use of Bitwise OR(|) operator.
print("B. a | b =", a | b)

# Use of Bitwise XOR(^) operator.
print("C. a ^ b =", a ^ b)

# Use of shift(left) operator.
print("D. a << 2 = ", a << 2,"and","b<<2=",b<<2)

# Use of shift(both) operator.
print("E. a >> 2 = ", a >> 2, " and ", "b >> 4 = ", b >> 4)

#4
# Taking input
string = str(input("Enter any string: "))

# Using string slicing to find a word in the string
checked = string.find("name")

# Making a loop for printing yes and no for the required outputs.
# Here '==' is comparison operator
if checked == -1:  # '-1' is the value as an output of find function indicating the absence of particular string in it.
    print("No")

else:
    print("Yes")

#5
# Taking inputs of the sides of the triangle.
n1 = int(input("Enter First length : "))
n2 = int(input("Enter Second length : "))
n3 = int(input("Enter Third length : "))

# Checking the condition for triangle to be formed.
F1 = n1 > n2 + n3
F2 = n2 > n1 + n3
F3 = n3 > n1 + n2

# Here we check wheather the all conditions are satisfied or not.
Output = str(F1 or F2 or F3)

print("The triangle can be formed?")

# Using string slicing.
print(Output.replace("True", "No!").replace("False", "Yes!"))

#6
number_1 = int(input("Enter 1st number (a) "))

number_2 = int(input("Enter 2nd number (b) "))

"""Using 'exor' function because it gives output "0" for same input values (0 0 and 1 1) and output 1 for different input values (0 1 and 1 0)
Therefore, in two numbers, when we'll have different values at a bit, we will get 1 and we will need to replace that bit in the original number to make the numbers same
We will count the number of 1 s that come in binary after 'exor' operation to check how many bits we need to flip to convert 'a' to 'b' as asked in question
"""

ex_or = number_1 ^ number_2


bin_exor = bin(ex_or)
check_string = str(bin_exor)


bits_need_flip = check_string.count("1")

print("Number of bits needed to be flipped to convert ‘a’ to ‘b’ are:", bits_need_flip)
