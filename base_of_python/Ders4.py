# text = "Python kursumuza Hoş Geldiniz. Ben Arafat. Emin"
# text2 = ["apple", "banana", "cherry"]
#sonuc = text.upper()
# sonuc = text.lower()
# sonuc = text.capitalize()

# sonuc = "q".islower()

# sonuc = "    abc ".strip()
# sonuc = text.split()
# sonuc = text.split('.')
# sonuc1 = "Arafat"
# sonuc1 = text.join(sonuc1)

# index = text.index('kursumuza')
# sonuc = text.startswith('P')
# sonuc = text.endswith('a')

# text.reverse()
# sonuc = text.replace('Arafat','Mustafa')

# sonuc = text.lower().replace(' ', '_').replace('arafat', 'ahmet').replace('.', '').replace('emin', 'berk')

# print(sonuc)



# Tuple

# tuple1 = ("apple", "banana", "cherry")
# tuple2 = ('a', 'c', 'b', 'a')

# tuple3 = tuple1 * 5
# tuple4 = tuple1 + tuple2
# print(tuple3)
# print(tuple4)

#
# print(tuple2.count('a'))
# print(tuple2.index('b'))

# my_Tuple = list(tuple)
# my_Tuple[2] = 10.0
# print(type(my_Tuple))
# str(my_Tuple.sort())
# print(my_Tuple)

# print(tuple)
# sonuc1 = tuple[:]
# sonuc2 = tuple[:2]
# sonuc3 = tuple[2:]
# sonuc4 = tuple[-1]
# sonuc5 = tuple[1:3]
# print(tuple)
# print(sonuc1)
# print(sonuc2)
# print(sonuc3)
# print(sonuc4)
# print(sonuc5)
# print(type(tuple[2]))
# print(len(tuple))



# Set
# set = {"abc", 34, "male", 40}
# # print(set)
# # for i in set:
# #     print(i, end=" ")
#
# x = set.pop()
# print(x)
# print(set)




library = {
    "name": "base_of_python",
    "surname": "Berk Dursun",
    "age": 21,
    "student": {
        "degree": 3,
        "department": "computer enginering",
        "favory": "chess"
    },

    "student2": {
        "degree": 4,
        "department": "computer enginering",
        "favory": "spor"
    }

}

# print(library)
# print(type(library))
# print(len(library))
#
# a = library["name"]
# b = library["surname"]
# c = library["age"]
# print(a)
# print(b)
# print(c)
#
#
# s1 = library.keys()
# s2 = library.values()
# s3 = library["student"].keys()
# s4 = library["student"]["department"]
# s5 = library["student"]["favory"]
# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(" ")


# for i in library:
#     print(i)
# print("")
#
# for i in library.keys():
#     print(i)
# print("")
#
#
# for i in library.values():
#     print(i)
# print("")
#
# for i in library.items():
#     print(i)
# print("")

# library["student"]["favory"] = "Learn Python"
# print(library)
#
# library.update({"salary": 30000})
# print(library)
#
#
# library.update({"surname": "Dursun"})
# print(library)


# p = library.pop("salary")
# print(p)
# print(library)


# print(library)
# p = library.popitem() # random item siliniyo
# print(p)
# print(library)



# library.clear()
# print(library)

# del library
# print(library)



# my_dictionary1 = library.copy()
# print(my_dictionary1)
# print(type(my_dictionary1))
#
# my_dictionary2 = dict(library)
# print(my_dictionary2)
# print(type(my_dictionary2))



