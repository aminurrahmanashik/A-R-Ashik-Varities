
file_counts = {"jpg":10,"txt":14,"csv":2,"py":23}
list1 = file_counts.keys()
list2 = file_counts.values()
print(list1)
print(list2)

# example of counting how many times each letter appears in a piece of text.
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


text = input("Enter your text:")
ans = count_letters(text)
print(ans)