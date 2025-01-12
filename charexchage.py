str1=input("Enter a string: ")
def exchange(str1):
    first_char=str1[0]
    last_char=str1[-1]
    resulting_string=last_char+str1[1:-1]+first_char
    print(resulting_string)
exchange(str1)
