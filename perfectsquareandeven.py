start=int(input("Enter the starting 4-digit no : "))
end=int(input("Enter the ending 4-digit no : "))
rangelist=[]
startrange=(start**0.5)
endrange=(end**0.5)
for i in range(startrange,endrange+1):
    square=i**2
    if square%2==0:
        print(square,end=" ")
