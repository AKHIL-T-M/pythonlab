list1=input("Enter the colors in list1: ").split()
list2=input("Enter the colors in list2: ").split()
def check_list(list1,list2):
    list3=set(list1)-set(list2)
    print(f"The colors are:{list3}")
check_list(list1,list2)
