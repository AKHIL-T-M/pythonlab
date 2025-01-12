N=int(input("Enter the number: "))
for i in range(1,N+1):
    if N % i == 0:
        print(i,end=" ")
