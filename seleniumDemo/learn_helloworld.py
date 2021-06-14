# 内容：基本语法学习

# 字符串
print('I\'m \"OK\"!')
print('I\'m learning\nPython.')  # \n
print('i am  %s and %s' % ('Test', 'Developer')) # i am  Test and Developer
print(r'\\\t\\')  # 用r''表示''内部的字符串默认不转义
print('''line1
line2
line3''')

print(r'''hello,\n
world''')

# 布尔值  区分大小写 and、or和not运算
print(True and False)
print(1 > 2)
print(not 1 > 2)

# None 不能理解为0，因为0是有意义的，而None是一个特殊的空值
print(None)

# 变量 变量名必须是大小写英文、数字和_的组合，且不能用数字开头
a = 123  # a是整数
print(a)
a = 'ABC'  # a变为字符串
print(a)

a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量 通常用全部大写的变量名表示常量
PI = 3.14159265359

# 整数的除法为什么也是精确的？
# 除法1
print(10 / 3)
# 除法2
print(10 // 3)

print(10 % 3)

# 字符串编码
print(ord('A'))  # 编码
print(chr(65))  # 解码
print('\u4e2d\u6587')
print('中文', len('中文'))
print('中文encode', len('中文'.encode('utf-8')))
print(len('ABC'))

# 格式化
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# list
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[-2])  # 获取
classmates.append('Adam')  # 添加
print(classmates)
classmates.insert(1, 'Jack')  # 指定位置插入
print(classmates)
classmates.pop()  # 删除list末尾的元素
print(classmates)
classmates.pop(1)  # 删除指定位置
print(classmates)

# tuple 另一种有序列表叫元组
t = (1)
print(t)  # 定义的不是tuple，是1这个数
t = (1,)
print(t)  # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义

# 条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# s = input('birth: ')
# birth = int(s)  # input()返回的数据类型是str
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 循环
# for循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# while循环  计算100以内所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break 提前结束循环
n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue  跳出当前这次循环，开始下一次循环
# 只打印奇数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

list(range(5))  # [0, 1, 2, 3, 4] 从0开始小于5的整数集合

# dict 字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
d['Adam'] = 67
print(d['Adam'])
print('Thomas' in d)  # 通过in判断key是否存在
print(d.get('Thomas'))  # key不存在，可以返回None，或者自己指定的value
print(d.get('Thomas', -1))
d.pop('Bob')  # 删除一个key
print(d)

# set
s = set([1, 2, 3])
print(s)
s = set([1, 1, 2, 2, 3, 3])  # 重复的key会过滤
print(s)
s.add(4)  # 添加元素
print(s)
s.add(4)
print(s)
s.remove(4)  # 删除元素
print(s)

s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)  # 交集
print(s1 | s2)  # 并集

# 函数
print(abs(-20))  # 求绝对值的函数abs
print(max(2, 3, 1, -5))  # 求最大值
print(int('123'))  # 其他数据类型转换为整数

# 定义函数
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x

print(my_abs(-99))

def nop():
    pass  # 定义一个什么事也不做的空函数，可以用pass语句

# 返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# 函数的参数
# 计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(5, 2))  # power(x, n=2)可以用power(5)，但是power(x, n) 不能用power(5)



x = 'runoob';
for i in range(len(x)):
    print(x[i])

print("类型：", type(range(1, 5)))
print(range.mro())
