N=int(input("Enter the no of elements: "))
list=[]
for i in range(N):
    val=input(f"Enter the string {i+1}:")
    list.append(val)
def long(list):
    max_size=0
    longest_word=""
    for i in list:
        if len(i)>max_size:
            max_size=len(i)
            longest_word=i
    return longest_word,max_size
print(f"The longest element and its size is:{long(list)}")
