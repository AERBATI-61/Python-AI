import numpy as np
result1 = np.array([1, 2, 3, 4, 5])
result2 = np.arange(1, 10)
result3 = np.arange(10, 100, 3)
result4 = np.zeros(10)
result5 = np.ones(10)
result6 = np.linspace(0, 100, 5)
result7 = np.linspace(0, 5, 5)
result8 = np.random.randint(0, 10)
result9 = np.random.randint(0, 10)
result10 = np.random.randint(20)
result11 = np.random.randint(1, 10, 3)
result12 = np.random.rand(5)
result13 = np.random.randn(5)



result14 = np.arange(50)
result15 = result14.reshape(5, 10)
result16 = result15.sum(axis=1)
result17 = result15.sum(axis=0)
print(result15)
print("Satirlarin toplami", result16)
print("Sutunlerin toplami", result17)



result18 = np.random.randint(0, 100, 10)
print(result18)
result19 = result18.max()
result20 = result18.min()
result21 = result18.mean()
result22 = result18.argmax()
result23 = result18.argmin()
result24 = result18.argsort()
print(result24)





