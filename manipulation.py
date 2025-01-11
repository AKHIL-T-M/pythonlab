#over 100
A=int(input("enter the range: "))
list=[]
for i in range(A):
    value=int(input("Enter the value: "))
    list.append(value)
for i in range(len(list)):
    if(list[i]>100):
        list[i]="over"
print(list)
#same length
string1=[int(x) for x in input("Enter a string1: ").split()]
string2=[int(x) for x in input("Enter the string2: ").split()]
if(len(string1)==len(string2)):
    print("list are of same length!")
else:
    print("list are not of same length!")
#same sum
string3=[int(x) for x in input("Enter a string3: ").split()]
string4=[int(x) for x in input("Enter the string4: ").split()]
if(sum(string3)==sum(string4)):
    print("same sum")
else:
    print("not same")
#same value
string5=[int(x) for x in input("Enter a string5: ").split()]
string6=[int(x) for x in input("Enter a string6: ").split()]
def check_lists(string5,string6):
    x=set(string5)&set(string6)
    if(x):
        print("Common values found in both lists:",x)
    else:
        print("No common values found in both lists:",x)
check_lists(string5,string6)
