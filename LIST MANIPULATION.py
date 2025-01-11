#For all values greater than 100,store 'over'
#Algorithm
#step 1 : start 
#step 2 : Ask the user to enter number of elements in list
#step 3 : Ask the user to enter the integers
#step 4 : if intger > 100 then replace the value as 'over'
#step 5 : print proper result
#step 6 : stop

d=[]
num=int(input("Enter number of elements in the list : "))
print("Enter the Elements : ")
for i in range(0,num):
    element=int(input())
    d.append(element)
for i in range(len(d)):
    if d[i]>100:
        d[i]="over"
print(d)
<----------OUTPUT----------->
Enter number of elements in the list : 4
Enter the Elements :
100
55
500
400
[100, 55, 'over', 'over']

#Whether lists are of Same length
#step1:start
#step2:Ask the user to enter numbers in two list both seperated by spaces
#step3:using len(),check if length of list1 equals to list2,then they are same length else not
#step4:print proper result
#step5:stop

list1 = [int(x) for x in input("Enter Elements of the first list separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter Elements of the second list separated by spaces: ").split()]
def check_lists(list1, list2):
    if len(list1) == len(list2):
        print("Both lists are of the same length.")
    else:
        print("Lists are not of the same length.")
check_lists(list1, list2)
<----------OUTPUT----------->
Enter Elements of the first list separated by spaces: 1
Enter Elements of the second list separated by spaces: 2 3 4 5
Lists are not of the same length.


#whether list sums to same value
#step1:start
#step2:Ask the user to enter numbers in two list both seperated by spaces
#step3:Using sum(),if sum of list1 equals to lsit2 ,then their sums are equal else not
#step4:print proper result
#step5:stop
list1 = [int(x) for x in input("Enter Elements of the first list separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter Elements of the second list separated by spaces: ").split()]
def check_lists(list1, list2):
    if sum(list1) == sum(list2):
            print("Both lists have the same sum.")
    else:
            print("Lists do not have the same sum.")
check_lists(list1, list2)
<----------OUTPUT----------->
Enter Elements of the first list separated by spaces: 4 5
Enter Elements of the second list separated by spaces: 1 5
Lists do not have the same sum.

#whether any value occur in both
#step1:start
#step2:Ask the user to enter numbers in two list both seperated by spaces
#step3:Using set() ,find the common value
#step4:print proper result
#step5:stop
list1 = [int(x) for x in input("Enter Elements of the first list separated by spaces: ").split()]
list2 = [int(x) for x in input("Enter Elements of the second list separated by spaces: ").split()]

def check_lists(list1, list2):
    common_values = set(list1) & set(list2)
    if common_values:
        print("Common values found in both lists:", common_values)
    else:
        print("No common values found in both lists.")
check_lists(list1, list2)
<----------OUTPUT----------->
Enter Elements of the first list separated by spaces: 1 4
Enter Elements of the second list separated by spaces: 2 4
Common values found in both lists: {4}