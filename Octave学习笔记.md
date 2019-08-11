# Octave学习

>消除左侧octeve行号及提示，结尾加 ';' 当前不输出

![1564055520799](C:\Users\Liar\AppData\Roaming\Typora\typora-user-images\1564055520799.png)

```octave
PS1('>>');
```

------


> 输出数值

```octave
>>a = pi;
>>disp(a)
3.1416
>>disp(sprintf('6 decimals: %0.6f' ,a)) %类似c语言格式化输出到小数点后6位
6 decimals: 3.141593
```

-----

> 输入矩阵

```octave
A = [1 2 ; 3 4 ; 5 6] %输入三行两列的矩阵
V = 1:0.1:2 %输入向量，步长为0.1，范围1-2
ones(2,3) %元素全为1的矩阵
zeros(2,3) %0矩阵
rand(3,3) %随机数矩阵
eye(4) %4阶单位矩阵
```

-----

> 打印图表

```octave
hist(w)
```

-----

> 变量显示与删除

```octave
whos %显示工作空间所有变量
clear %删除工作空间所有变量
A(2,:) %显示矩阵第二行所有数值
A(:,3) %显示矩阵第三列所有数值
```

-----

> 载入文件与保存

```octave
save hello.mat A %保存A变量为hello.mat文件
load hello.mat %载入hello.mat文件并赋给变量A
save hello.txt A -ASCII %保存变量A为ASCII编码的txt文件
```

# 