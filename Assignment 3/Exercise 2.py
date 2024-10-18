def generate_words(list, n, str="", words=[]):
    if len(str) == n:
        words.append(str)  # Base case: combination of length n is complete
        return

    for i in list:
        generate_words(list, n, str + i)  # Recursive call

    return words

# Example
list = ["a", "b", "c"]
n = 3
result = generate_words(list, n)

for j in result:
    print(j)