import numpy as np

"""
result = np.arange(5, 15)
print(result)

result1 = np.arange(50, 100, 5)
print(result1)

result2 = np.zeros(10)
print(result2)

result3 = np.ones(10)
print(result3)

result4 = np.linspace(0, 100, 5)
print(result4)

result5 = np.random.randint(10, 30, 5)
print(result5)




result7 = np.linspace(1, -1, 10)
print(result7)



result8 = np.random.randint(10, 50, 15)
result9 = result8.reshape(3, 5)
print(result8)
print(result9)


result10 = np.random.randint(0, 100, 10)
result11 = np.random.randint(0, 100, 10)

result12 = result11 + result10
print(result10)
print(result11)
print(result12)
result13 = result10.max()
result14 = result11.min()
result15 = result11.mean()
print(result15)

result16 = np.random.randint(10, 20, 10)
print(result16)
print(result16[:3])
print(result16[::-1])

Numbers = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 100]])
print(Numbers)
print(Numbers**2)

netice17 = Numbers[:, 1:3]
netice18 = Numbers[:, 0]
netice19 = Numbers % 2 == 0
print(netice19)
"""

result = np.arange(0, 25)
result1 = result.reshape(5,5)
print(result1)

result1[2, 2] = 0
print(result1)




