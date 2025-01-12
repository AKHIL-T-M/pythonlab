str1=input("Enter a string: ")
str2=input("Enter another string: ")
first_char_str1=str1[0]
first_char_str2=str2[0]
changed_str1=first_char_str2+str1[1:]
changed_str2=first_char_str1+str2[1:]
print(changed_str1,changed_str2)
