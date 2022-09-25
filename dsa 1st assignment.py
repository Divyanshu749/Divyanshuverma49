class Node:
    def __init__(self,name=None,age=None):
        self.prev=None
        self.next=None
        self.name=name
        self.age=age
class doubleLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert(self,name,age):
        node=Node(name,age)
        if self.head is None:#no element present
            self.head=node
            self.tail=node
        else:# we will be adding the element at the end if its not the first
           temp=self.head
           while temp.next is not None:
            temp=temp.next
           node.prev=temp
           temp.next=node
           self.tail=node
print('Enter the no of family members:')
n= int(input())
names=n*[None]
ages=n*[None]
for i in range(0,n):
    print('Enter the name of family member:')
    names[i]=input()
    print('Enter the age of family member:')
    ages[i]=int(input())
for i in range(0,n):
    for j in range(0,n-i-1):
        if ages[j]<ages[j+1]:
            ages[j],ages[j+1]=ages[j+1],ages[j]
            names[j],names[j+1]=names[j+1],names[j]
FamilyTree=doubleLL()
for i in range(0,n):
    FamilyTree.insert(names[i],ages[i])
temp=FamilyTree.head
for i in range(0,n):#printing the familytree
    print('|Name: ',temp.name,' age: ',temp.age,'|  ---><------ ',end='')
    temp=temp.next
print('None')

    
    
    
            

