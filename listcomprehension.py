#+ve input
N=int(input("Enter the number of elements: "))
list=[]
for i in range(list):
    value=int(input("Enter the value:"))
    list.append(value)
positive=[i for i in list if i>0]
print(positive)
...............................................
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
word=input("enter the word:")
V="AaEeIiOoUu"
list=[char for char in word if char in V]
print(list)
#square
list2=[]
B=int(input("Enter the no of elements in list:"))
for i in range(B):
    value1=int(input("enter the no: "))
    list2.append(value1)
square=[i*i for i in list2]
print(square)
#ordinal value
list=input("Enter the string: ")
ordlist=[ord(i) for i in list]
print(ordlist)
.......................................
list3=[]
string=input("Enter the string")
for i in string:
    list3.append(ord(i))
print(list3)
