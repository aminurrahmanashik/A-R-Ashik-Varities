#Q-01 ok
# def format_address(address_string):
#     # Declare variables
#
#     # Separate the address string into parts
#
#     # Traverse through the address parts
#     words = address_string.split()
#     new_word = ""
#     # Determine if the address part is the
#     # house number or part of the street name
#
#     # Does anything else need to be done
#     # before returning the result?
#     for word in words:
#         if word != words[0]:
#             new_word += word + " "
#     # Return the formatted string
#     return "house number {} on street named {}".format(words[0], new_word)
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"

# #Q-02 ok
# def highlight_word(sentence, word):
#     new_sentence = ""
#     words = sentence.split(" ")
#     for wd in words:
#         new_word = ''.join(filter(str.isalpha, wd))
#         if new_word == word:
#             new_sentence = sentence.replace(new_word,new_word.upper())
#     return(new_sentence)
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))

# #Q-03 ok
# def combine_lists(list1, list2):
#     list1.reverse()
#     new_list = list2 + list1
#     return new_list
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))

# #Q-4 ok
# def squares(start, end):
# 	return [n*n for n in range(start,end+1)]
#
# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
#
# #Q-5 ok
# def car_listing(car_prices):
#   result = ""
#   for k,v in car_prices.items():
#     result += "{} costs {} dollars".format(k,v) + "\n"
#   return result
#
# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))
#
# #Q-6 ok
# def combine_guests(guests1, guests2):
#     new_dict = {}
#     guests2.update(guests1)
#     return guests2
#   # Combine both dictionaries into one, with each key listed
#   # only once, and the value from guests1 taking precedence
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))
#
# #Q-7 ok
# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   for letter in text:
#       if letter.isalpha() and letter in result:
#         result[letter.lower()] += 1
#       elif letter.isalpha():
#         result[letter.lower()] = 1
#
#   return result
#
# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
#
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
# #Q-8 ok
# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

# # #Q-09
# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)

# #Q-10 ok
# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())