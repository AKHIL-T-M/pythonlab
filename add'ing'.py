str1=input("Enter a string: ")
def modif(str1):
    if str1.endswith('ing'):
        return str1+'ly'
    elif str1[-1]=='e':
        return str1[0:-1]+'ing'
    else:
        return str1+'ing'
print(modif(str1))
