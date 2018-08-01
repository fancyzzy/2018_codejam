print('***find the defference between two chars***')
s = input("please input a string s = ")
t = input("please input a string t = ")
print('=====================================================')
def find_char():
    l1 = len(s)
    l2 = len(t)
    List = []

    if l2 != l1+1:
        input("please input again t = ")
    elif l1 > 1000:
        print("The length of the char no more than 1000!")
        input("please input again s = ")
    elif l2 > 1000:
        print("The length of the char no more than 1000!")
        input("please input again t = ")

    list1 = list(s)
    list2 = list(t)
    while '\n' in list1 and list2:
        list1.remove('\n')
        list2.remove('\n')
    list1 = sorted(list1)
    list2 = sorted(list2)

    i = 0
    for char in range(l1):
        if list1[i] == list2[i]:
            i += 1
        else:
            List.append(list2[i])
    if List == []:
        List.append(list2[-1])
    print(List)

findChar = find_char()