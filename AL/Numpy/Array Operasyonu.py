import numpy as np
number1 = np.random.randint(10, 100, 6)
number2 = np.random.randint(10, 100, 6)
result1 = number2 + number1
result2 = number2 - number1
result3 = number2 * number1
result4 = number2 / number1
result5 = number2 * 10
result6 = np.sin(number1)
result7 = np.cos(number1)
result8 = np.log(number1)
result9 = np.sqrt(number1)
# print(number1)



# mnumbers1 = number1.reshape(2, 3)
# mnumbers2 = number2.reshape(2, 3)
# print(mnumbers1)
# print(mnumbers2)
# dikey_birlestir = np.vstack((mnumbers1, mnumbers2))
# yatay_birlestir = np.hstack((mnumbers1, mnumbers2))
# print(dikey_birlestir)
# print(yatay_birlestir)

print(number1)
compare1 = number1 >= 50
compare2 = number1 % 2 == 0
print(compare2)
print(number1[compare2])