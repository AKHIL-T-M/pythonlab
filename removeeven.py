string1=[int(x) for x in input("Enter the integer values: ").split(',')]
print(string1)
list=[]
for i in string1:
    if(i%2!=0):
        list.append(i)
print(f"The resulting list is: {list}")
