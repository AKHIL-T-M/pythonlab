number=int(input("Enter a number: "))
factorial=1
for i in range(1,number+1):
    factorial*=i
print(f"THE factorial of number {number} is :{factorial}")
