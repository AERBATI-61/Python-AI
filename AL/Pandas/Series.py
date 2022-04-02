import pandas as pd
import numpy as np
numbers1 = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
scalar = 5
dict = {
    'a': 10,
    'b': 20,
    'c': 30,
    'd': 40,
    'e': 50
}
random_numbers = np.random.randint(10, 100, 5)
print(random_numbers)
print(pd.Series(random_numbers))
print(pd.Series(dict))


# pandas_series1 = pd.Series(numbers1)
# pandas_series2 = pd.Series(letters)
# pandas_series3 = pd.Series(scalar, [1, 2, 3, 4, 5])
# pandas_series4 = pd.Series(numbers1, letters)
# pandas_series5 = pd.Series(dict)
# pandas_series6 = pd.Series(random_numbers)
#
# print(pandas_series1)
# print(pandas_series2)
# print(pandas_series3)
# print(pandas_series4)
# print(pandas_series5)
# print(pandas_series6)
#
#
pandas_series4 = pd.Series(numbers1, letters)
# print(pandas_series4['a'])
# result1 = pandas_series4[0]
# result2 = pandas_series4[-1]
# result3 = pandas_series4[2:]
# result4 = pandas_series4[-2:]
# result5 = pandas_series4[::]
# result6 = pandas_series4['a']
# result7 = pandas_series4['e']
# result8 = pandas_series4[['a', 'e', 'c']]
# print(result1)
# print(result2)
# print(result3)
# print(result4)
# print(result5)
# print(result6)
# print(result7)
# print(result8)
#
#
#
# pandas_series = pd.Series(numbers1, letters)
# sonuc1 = pandas_series.ndim                         # kac boyutlu dizi oldugunu veriyor.
# sonuc2 = pandas_series.dtype
# sonuc3 = pandas_series.shape                        # kac elemanli ve kac boyutlu oldugunu veren ozellik
# sonuc4 = pandas_series.sum()
# sonuc5 = pandas_series.max()
# sonuc6 = pandas_series.min()
# sonuc7 = pandas_series + pandas_series
# sonuc8 = pandas_series + 100
# sonuc9 = np.sqrt(pandas_series)
# sonuc10 = pandas_series >= 2
# sonuc11 = pandas_series % 2 == 1
#
#
# print(sonuc1)
# print(sonuc2)
# print(sonuc3)
# print(sonuc4)
# print(sonuc5)
# print(sonuc6)
# print(sonuc7)
# print(sonuc8)
# print(sonuc9)
# print(sonuc10)
# print(sonuc11)
# print(pandas_series[sonuc10])
#
#
#
#
# volvo2021 = pd.Series([1, 2, 3, 4, 5], ["v1", "v2", "v3", "v4", "v5"])
# volvo2022 = pd.Series([4, 2, 3, 1, 5], ["v1", "v2", "v33", "v4", "v5"])
#
# total = volvo2021 + volvo2022
# print(total)
# print(total["v3"])
# print(total["v2"])