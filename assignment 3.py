''' Name  : Divyanshu Verma
    SID    : 21107109
    Branch : Mechanical   '''
import math

print('Ans-1 :-')
n = int(input('Enter a number: '))
print(f'Binary equivalent of {n} is', bin(n)[2:])

print('Ans-2 :-')
a = input('Enter expression: ')
print(a, '=', eval(a))

print('Ans-3:-')
print("a) (3+4)(5) = ", (3 + 4) * 5)
n = int(input("Enter an integer = "))
print('b)', n / 2 * (n - 1))
r = int(input('Enter radius ='))
print('c)', 4 * math.pi * r * r)
a = int(input('Enter angle 1 = '))
b = int(input('Enter angle 2 = '))
print('d)', math.sqrt((r * math.cos(a) * 2) + (r * math.sin(b) * 2)))

x1 = int(input('Enter x coordinate of first point: '))
y1 = int(input('Enter y coordinate of first point: '))
x2 = int(input('Enter x coordinate of second point: '))
y2 = int(input('Enter y coordinate of second point: '))
print('e)', (y2 - y1) / (x2 - x1))

print('Ans-4 :-')
print('4.(a)')
for i in range(5):
    print(i)
print('4.(b)')
for i in range(3, 10):
    print(i)
print('4.(c)')
for i in range(4, 13, 3):
    print(i)
print('4.(d)')
for i in range(15, 5, -2):
    print(i)
print('4.(e)')
for i in range(5, 3):
    print(i)

print('Ans-5:-')
C = int(input('Enter number of carbon atoms in molecule: '))
H = int(input('Enter number of hydrogen atoms in molecule: '))
O = int(input('Enter number of oxygen atoms in molecule: '))
print('The molecular weight of the compound is', H * 1.00794 + C * 12.0107 + O * 15.9994)