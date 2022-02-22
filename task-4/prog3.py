"""
Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
pip install tabulate

"""
from tabulate import tabulate
Table=[]
for i in range(3):
    l1=[]
    RollNo=int(input())
    Name=input()
    Marks=int(input())
    l1.append(RollNo)
    l1.append(Name)
    l1.append(Marks)
    Table.append(l1)
print(tabulate(Table, headers=["Roll No", "Name", "Marks"]))
output=int(input("Enter the index: "))
for i in range(len(Table[output-1])):
    print(Table[output-1][i],end=" ")
    
