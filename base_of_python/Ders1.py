import test

ahmet = """
            y
            o
            r
            u
            m
        """
print(ahmet)


a = 1
b = 1.5
c = "base_of_python"
d = True
e = False




print("Ben", type(a), "Degerim: ", a)
print("Ben", type(b), "Degerim: ", b)
print("Ben", type(c), "Degerim: ", c)
print("Ben", type(d), "Degerim: ", d)
print("Ben", type(e), "Degerim: ", e)




f = int(e)
g = float(a)
h = int(b)
i = str(a)

print("Ben", type(f), "Degerim: ", f)
print("Ben", type(g), "Degerim: ", g)
print("Ben", type(h), "Degerim: ", h)
print("Ben", type(i), "Degerim: ", i)




name1 = "Arafat"
name2 = name3 = "base_of_python"
name4, name5, name6 = "Meryem", "Osman", "Muhammed"

print(name1, name2, name3)
print(name4, name5, name6)
print(name4 + " " + name1, "in Kizi")



number1 = 10.0
number2 = 3.0
result1 = number1 + number2
result2 = number1 - number2
result3 = number1 * number2
result7 = number1 ** number2
result4 = number1 / number2
result5 = number1 // number2
result6 = number1 % number2

print(result1 + result6)
print(result2 - result4)
print(result3 * result5)
print(result4 / result1)
print(result5 // result3)
print(result6 % result2)
print(result7)


acik_div_sayisi = test.arafat.count('<div')
kapali_div_sayisi = test.arafat.count('</div>')
kapali_div_sayisi2 = test.ahmet.count('m')
print("Acik div sayisi: ", acik_div_sayisi)
print("Kapali div sayisi: ", kapali_div_sayisi)
print("Kapali div sayisi: ", kapali_div_sayisi2)









