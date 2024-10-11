list1 = [54, 76, 2, 4, 98, 100]
int1 = int(input())
int2 = int(input())
if int1 < int2:
    for i in range(len(list1)):
        if int1 <= list1[i] <= int2:
            print(list1[i])
else:
    for i in range(len(list1)):
        if int2 <= list1[i] <= int1:
            print(list1[i])