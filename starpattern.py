N=int(input("Enter the size of star pyramid: "))
for i in range(1,N+1):
    for j in range(i):
        print("*",end=" ")
    print("\n")
for i in range(N,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\n")
