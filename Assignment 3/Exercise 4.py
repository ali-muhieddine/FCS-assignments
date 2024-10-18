sorted_list = list(map(int, input("Enter a sorted list of integers (space-separated): ").split()))
n = int(input("Input a number: "))
sorted_list.append(n)
sorted_list.sort()

print(sorted_list)