list=[]
n=int(input("Enter the no of elements: "))
for i in range(n):
    value=input(f"enter the string {i+1}")
    list.append(value)
count=0
for i in list:
    count+=i.lower().count('a')
print(f"the no of occurence is:{count}")
