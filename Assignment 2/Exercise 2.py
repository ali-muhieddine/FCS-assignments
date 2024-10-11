names = ['Maria', 'Hala', 'Ghady', 'Ehsan', 'Joe', 'Zoe']
letter = input()
for i in range(len(names)):
    if letter in names[i]:
        print(names[i])

