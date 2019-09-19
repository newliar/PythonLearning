# d = {'a':1, 'b':2, 'c':3}
# for key in d :
#     print(key)

# for ch in 'ABC':
#     print(ch)

# list(range(1,11))


n = input()
n = int(n)
list1 = []
list1 = input().split()
list2 = []
i = 0
while i < n:
    m = int(list1[i])
    list2.append(m)
    i += 1
print(list2)
