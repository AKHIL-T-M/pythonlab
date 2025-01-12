word=input("Enter the string: ").lower()
freq={}
for i in word:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
