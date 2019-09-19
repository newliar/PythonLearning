# 在N行M列的正整数矩阵中，要求从每行中选出1个数，
# 使得选出的总共N个数的和最大。
# 输入：
# 第一行两个正整数N和M，用空格隔开，表示行数和列数
# 第2行到第N+1行，每行M个用空格隔开的整数 ，表示矩阵
# 输出
# 最大总和

print("输入行数和列数")
N,M = map(int,input().split())
list = []
total = 0
for i in range(0, N):
    list = input().split()
    max = int(list[0])
    for j in range(1,M):
        m = int(list[j])
        if m > max:
            max = m
    total=total+max
print(total)
    
