N=int(input("Enter the no of elements: "))
list=[]
for i in range(N):
    value=int(input(f"Enter the elements {i+1}:"))
    list.append(value)
sum=0
for i in list:
    sum+=i
print(f"the sum of list is :{sum}")
