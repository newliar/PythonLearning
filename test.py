# for i, value in enumerate(['A' ,'B', 'C']):
#     print(i, value)
# for x, y in [(1, 1), (2, 4), (3, 9)]:
#     print(x, y)

# # L = [x * x for x in range(1, 11)] #列表生成式
# L= [x for x in range(0,100) if x%2==0]

# print(L)

g = (x * x for x in range(10))
for x in g:
    print(x)