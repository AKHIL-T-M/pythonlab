#+ve input
N=int(input("enter element no:"))
list=[]
A="AaEeIiOoUu"
for i in range(N):
    value=int(input("entwer"))
    list.append(value)
for i in list:
    if i>0:
        print(i)
#vowels
word=input("string:")
list1=[char for char in word if char in A]
print(list1)
#square
list2=[]
B=int(input("Enter the no of elements in list:"))
for i in range(B):
    value1=int(input("enter the no: "))
    list2.append(value1)
square=[i*i for i in list2]
print(square)
#ordinal value
list3=[]
string=input("Enter the string")
for i in string:
    list3.append(ord(i))
print(list3)
