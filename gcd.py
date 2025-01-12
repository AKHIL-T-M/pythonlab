str1=int(input("Enter the number1: "))
str2=int(input("Enter the number2: "))
def find_gcd(str1,str2):
    i=1
    while(str1>=i and str2>=i):
        if(str1%i==0 and str2%i==0):
            gcd=i
        i=i+1
    print(gcd)
find_gcd(str1,str2)
