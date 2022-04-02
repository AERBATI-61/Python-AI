'''
#count, [append, insert], [remove, pop], [sort, reverse], copy, index, [max, min,], len, [ del, clear]

List        -> is a collection which is ordered and changeable. Allows duplicate members.               []
Tuple       -> is a collection which is ordered and unchangeable. Allows duplicate members.             ()
Set         -> is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.  {}
Dictionary  -> is a collection which is ordered** and changeable. No duplicate members.                 {}
'''

ahmet1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ahmet1[2] = 20
print(ahmet1)
ahmet2 = "is a collection which is ordered** and changeable. No duplicate members".split()
ahmet3 = ["is", "a", "collection"]
print(ahmet1)
print(ahmet2)
print(ahmet1[::-1])
print(ahmet2[::-1])
print(ahmet1[0])
print(ahmet2[0])
print(ahmet1[-1])
print(ahmet2[-1])
print(ahmet1[2:5])
print(ahmet2[2:])

if "No" in ahmet2:
    print("There is the word")
else:
    print("There isn't word")

for i in ahmet1:
    if i == 5:
        print(i, end="____")

print()
ahmet4 = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(ahmet4[2][0])


ahmet5 = [1, 20, 2, 4, -1, 2]
print(ahmet5[1])


# func1 = ahmet5.count(2)
# say = 0
# for i in ahmet5:
#     if i == 2:
#         say += 1
# print("ben say", say)
#
# ahmet5.append(3)
# ahmet5.insert(3, 3)
# ahmet5.insert(-1, 10)
# ahmet5.pop()
# ahmet5.pop(3) #index alir
# ahmet5.remove('ikki')
# ahmet5.remove(10)


ahmet5.sort()
ahmet5.reverse()


ahmet6 = ahmet5.copy()

ahmet7 = ahmet5.index(2)

ahmet8 = max(ahmet5)
ahmet9 = min(ahmet5)



print(ahmet5, "\n", ahmet8, ahmet9)
print(len(ahmet5))
print("ben birinci ahmet6 ",ahmet6)
del ahmet6

print("ben birinci ahmet5 ", ahmet5)
ahmet5.clear()
print("ben ikinci ahmet5 ", ahmet5)

