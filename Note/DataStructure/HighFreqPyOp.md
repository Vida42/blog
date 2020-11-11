# Python Collections

<table>
<tr>
    <td><b> Name </b></td>
    <td><b> Ordered </b></td>
    <td><b> Changeable </b></td>
    <td><b> Indexed </b></td>
    <td><b> Duplicated </b></td>
</tr>

<tr>
    <td> List </td>
    <td> :heavy_check_mark: </td>
    <td> :heavy_check_mark: </td>
    <td> :heavy_check_mark: </td>
    <td> :heavy_check_mark: </td>
</tr>
<tr>
    <td> Tuple </td>
    <td> :heavy_check_mark: </td>
    <td> :x: </td>
    <td> :heavy_check_mark: </td>
    <td> :heavy_check_mark: </td>
</tr>
<tr>
    <td> Set </td>
    <td> :x: </td>
    <td> :x: </td>
    <td> :x: </td>
    <td> :x: </td>
</tr>
<tr>
    <td> Dictionary </td>
    <td> :x: </td>
    <td> :heavy_check_mark: </td>
    <td> :heavy_check_mark: </td>
    <td> :x: </td>
</tr>

</table>

# Python List Comprehension

- usual

```python
if a>b:
    c = a
else:
    c = b
```

- list comprehension

```python
c = a if a>b else b
```

让两个list中的偶数分别相加，结果应是2+6,4+6,2+8,4+8:

```python
x=[1,2,3,4]
y=[5,6,7,8]

[a + b for a in x for b in y if a%2 == 0 and b%2 ==0]
```

如果for,if,else一起出现怎么办？

```python

[x for x in range(1, 10) if x % 2]

[ x if x%2 else x*100 for x in range(1, 10) ]

# You are using a filter in the first example.

# With a filter, you need:

[ EXP for x in seq if COND ]

# But in the second example you are only mapping each value to another
# (x if y else z is the syntax for the expression you're returning for each element)
# using a ternary-operator expression.

# Without a filter you need:

[ EXP for x in seq ]

```

# 编码

- 0-9数字的ASCII十进制编码为48-57

- 大写字母的ASCII十进制编码为65-90

- 小写字母的ASCII十进制编码为97-122

```python
# ord()函数就是用来返回单个字符的ascii值(0-255)
ord('d')
# >>> 100
# chr()函数是输入一个整数(0-255)返回其对应的ascii符号
chr(100)
# >>> 'd'
```

# 位运算符

```
a = 0011 1100
b = 0000 1101
```

```python
a&b = 0000 1100
# 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
a|b = 0011 1101
# 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
a^b = 0011 0001
# 按位异或运算符：当两对应的二进位相异时，结果为1
~a  = 1100 0011
# 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。
```

# Sorted

- sorted方法可接受三个参数：sorted(iterable, key, reverse), 如果不设置reverse，那么由小到大排序

- sort()接收两个参数sort(self,key,reverse)

```python
intervals = [[0,30],[15,20],[5,10]]
intervals = sorted(intervals, key=lambda x:x[0], reverse=True)

# >>> [[15, 20], [5, 10], [0, 30]]
```

time complexity for sort and sorted is O(n logn) average and worst case.


# Zip

```python
A = ["cbao","dafl","ghi"]
for i in zip(*A):
     print(i)
# ('c', 'd', 'g')
# ('b', 'a', 'h')
# ('a', 'f', 'i')

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = list(zip(a,c))     # 打包为元组的列表, 元素个数与最短的列表一致
print(zipped)
# [(1, 4), (2, 5), (3, 6)]
print(list(zip(*zipped)))   # 与 zip 相反，*zipped 可理解为解压，返回二维矩阵式
# [(1, 2, 3), (4, 5, 6)]
```

# reduce

reduce() 函数会对参数序列中元素进行累积

```python
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4,5])
```