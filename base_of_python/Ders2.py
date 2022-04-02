print('base_of_python')
print("base_of_python")

deger1 = "Hello"
deger2 = "World"
print(deger1 + " " + deger2)

name = "base_of_python.Berk"
surname = "Dursun"
age1 = 21
age2 = '21'
print(type(age1), age1)
ben1 = "Benim adim " + name + " Ve Soyadim " + surname + " Yasim ise " + str(age1)
a = str(age1)
print(type(a))
print(ben1)

ben2 = "Benim adim " + name + " Ve Soyadim " + surname + " Yasim ise " + age2
print(ben2)

print(name[0])
print(name[-1])
print(name[2:])
print(name[2:4])
print(name[1:7:2])
print(name[-3:-1])

name2 = """
 Whatis Lorem Ipsum?
 Lorem Ipsum is simply dummy 
 text of the printing and typesetting industry. 
 
"""

say = 0
for i in name2:
    if i == (" " or "?" or "." or ","):
        say += 1
    print(i, end=" ")
print(say)
print(len(name2))
print(name2.count("b"))
print(name2.capitalize())
print(name2.upper())
print(name2.lower())
print(name2.replace("Lorem", "base_of_python"))
print(name2.split(" "))

# \ etkisiz hale getirmek icin kullanilir.





print("Benim adim  {}   Ve Soyadim  {}   Yasim ise {}".format(name, surname, age2))
print("Benim adim  {0}   Ve Soyadim  {1}   Yasim ise {2}".format(name, surname, age2))
print("Benim adim  {2}   Ve Soyadim  {1}   Yasim ise {0}".format(name, surname, age2))
print("Benim adim  {n}   Ve Soyadim  {s}   Yasim ise {a}".format(n=name, s=surname, a=age2))
print(f"Benim adim  {name}   Ve Soyadim  {surname}   Yasim ise {age2}")





