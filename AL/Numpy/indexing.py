import numpy as np
numbers = np.array([0, 5, 10, 15, 20, 25, 50, 100])
# print(numbers)
result1 = numbers[1]
result2 = numbers[-1]
result3 = numbers[1:-1]
result4 = numbers[:-1]
result5 = numbers[1:]
result6 = numbers[::]
result7 = numbers[::-1]
result8 = numbers[::-2]
# print(result8)

Numbers = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 100]])
# print(Numbers)
netice1 = Numbers[0]
netice2 = Numbers[2]
netice3 = Numbers[0, 2]
netice4 = Numbers[2, 1]
netice5 = Numbers[:, 2]
netice6 = Numbers[:, 2] + Numbers[:, 1]
netice7 = Numbers[:, 0:2]
netice8 = Numbers[:, 0:2]
netice9 = Numbers[-1, :]
netice10 = Numbers[:2, :2]
# print(netice10)


arr1 = np.arange(0, 10)
arr2 = arr1   # Referance
print(arr1)
print(arr2)
arr2[0] = 20
print("")
print(arr1)
print(arr2)

# arr2 = arr1.copy() #adress
# print(arr1)
# print(arr2)
# print("")
# arr2[0] = 20
# print(arr1)
# print(arr2)
