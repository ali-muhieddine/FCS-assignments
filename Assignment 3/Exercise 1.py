def binarysearch(list, key):
    start = 0
    end = len(list)
    mid = (start+end)//2

    while end > start:
        if list[mid] == key:
            return True
        elif list[mid] > key:
            list = list[start:mid]
            return binarysearch(list, key)
        elif list[mid] < key:
            list = list[mid+1:end]
            return binarysearch(list, key)
    return False





#Example
list = [1, 2, 3, 4, 5, 6, 7, 12, 16, 22, 37, 65, 67, 102]
print(list)

print(binarysearch(list,12))

print(binarysearch(list,15))

print(binarysearch(list,67))