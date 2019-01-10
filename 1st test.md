19.1.9

# [LOCK]293. Flip Game
> Difficulty = Easy

## 分析

MMP又上锁，[这里](http://www.cnblogs.com/grandyang/p/5224896.html)看题
一个由任意个数`-`和`+`构成的字符串`-+-+++-+`，将其中的`++`替换为`--`，输出所有的可能。

那就循环……并且记住344中的python不支持item assignment

以下程序有些问题
```python
class Solution(object):
	def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		result = []
		s = list(s)
		count = 0
		for i in range(len(s)-1):
			if s[i] == '+' and s[i+1] == '+':
				result.append(s)
				result[count][i], result[count][i+1] = '-', '-'
				print(''.join(result[count]),'wtf')
				print(''.join(s))
				count += 1
		return result
```

```python
>>> lz = "-++++-++"
>>> ls = Solution().generatePossibleNextMoves(lz)
>>> print(ls)

---++-++ wtf
---++-++
------++ wtf
------++
-------- wtf
--------
```
s跟着result一起变了。`print(result[count] is s)`结果为`True`。原理我一时半会儿搞不清了，就记住不要随便改变原数据？总之改为以下后对了(能否AC不知)。


> **时间复杂度O(n)?**

```python
class Solution(object):
	def generatePossibleNextMoves(self, s):
		"""
		:type s: str
		:rtype: List[str]
		"""
		result = []
		for i in range(len(s)-1):
			if s[i] == '+' and s[i+1] == '+':
				middle = list(s)
				middle[i], middle[i+1] = '-', '-'
				result.append(''.join(middle))
		return result
```

shit，看题解少加一点判断是否为空(虽然也能执行，不过这还是个好习惯吧？)：
```python
if not s:
    return result
```

## 总结

中间操作过程可以更简单一点：
```python
result.append(s[:i]+'--'+s[i+2:])
```
如果`i+2`超出了字符串的索引，`lz[i+2:]`就返回一个`''`


# 205. Isomorphic Strings
> Difficulty = Easy

## 分析

要把s映射到t。分析以后发现条件就是：一个s不能映射成两个t，两个s也不能映射成一个t。

于是想到两字典双向判断即可。

> **时间复杂度O(n)？**

```python
# 76 ms, faster than 30.33%

class Solution:
	def isIsomorphic(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		dic1, dic2 = dict(), dict()
		for i in range(len(s)):
			# 检测同一字母是否映射成不同字母
			if s[i] in dic1:
				if dic1[s[i]] != t[i]:
					return False
			else:
				dic1[s[i]] = t[i]
			# 检测不同字母是否映射成同一字母
			if t[i] in dic2:
				if dic2[t[i]] != s[i]:
					return False
			else:
				dic2[t[i]] = s[i]
		return True
```

## 总结

1. 也可以写一个函数，调用两遍求and即可[[0]](https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/205._isomorphic_strings.md)

2. 用纸笔思考思路会清晰点。

[0] [Isomorphic Strings ApacheCN](https://github.com/apachecn/awesome-algorithm/blob/master/docs/Leetcode_Solutions/Python/205._isomorphic_strings.md)

# 345. Reverse Vowels of a String
> Difficulty = Easy

## 分析

只将字符串中的元音字母逆序输出

> **时间复杂度？**

two pointers
```python
class Solution:
	def reverseVowels(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		s = list(s)

		i, j, vowels =0, len(s)-1, ['a','e','i','o','u']
		while i < j:
			if s[i] in vowels and s[j] in vowels:
				s[i], s[j] = s[j], s[i]
			i += 1
			j -= 1
		return ''.join(s)
```

第一遍错
```python
Input	"hello"
Output	"hello"
Expected	"holle"
```

条件没理清，每个指针都分指到元音和没指到两种情况。改正：
```python
class Solution:
	def reverseVowels(self, s):
		s = list(s)
		i, j, vowels =0, len(s)-1, ['a','e','i','o','u']
		while i < j:
			if s[i] not in vowels:
				i += 1
			if s[j] not in vowels:
				j -= 1
			if s[i] in vowels and s[j] in vowels:
				s[i], s[j] = s[j], s[i]
				i += 1
				j -= 1
		return ''.join(s)
```

继续错：
```python
Input	"aA"
Output	"aA"
Expected	"Aa"
```

大写也算啊,加完大写字母对了
```python
# 124 ms, faster than 26.93%
```

## 总结

不总结了，看题解基本都是这个思想。
