## 10/7/20


278(找第一个错误版本)， 652(找K个最近)， 852(找峰顶)在用`lo = mid + 1`,`hi = mid - 1`频频出错，后来34也改为`lo = mid`和`hi = mid`也能过

## Before

Time Complexity in Coding Interview

• O(1) 极少
• O(logn) 几乎都是二分法
• O(√n) 几乎是分解质因数
• O(n) 高频
• O(nlogn) 一般都可能要排序
• O(n2) 数组，枚举，动态规划
• O(n3) 数组，枚举，动态规划

> np问题，通俗理解，只能用深度搜索解决的问题

• O(2n) 与组合有关的搜索
• O(n!) 与排列有关的搜索

比O(n)更优的时间复杂度几乎只能是O(logn)的二分法

Recursion or Non-Recursion

• 面试中是否使用 Recursion 的几个判断条件
1. 面试官是否要求了不使用 Recursion （如果你不确定，就向面试官询问）
2. 不用 Recursion 是否会造成实现变得很复杂
3. Recursion 的深度是否会很深
4. 题目的考点是 Recursion vs Non-Recursion 还是就是考你是否会Recursion？
• 记住：不要自己下判断，要跟面试官讨论！

搜索一般就是递归，其余情况尽量别用递归
链表不要用递归，深度会很深

while +1: avoid dead loop

二分，记得看是要找last还是first

outline
----

- 第一境界：会写程序：
    - Find First Position of Target
    - Find Last Position of Target
    - 34. Find First and Last Position of Element in Sorted Array

- 第二境界：二分位置 之 OOXX

> 找到第一个/最后一个满足某个条件的位置/值

    - 278. First Bad Version
    - 658. Find K Closest Elements
    - 702.Search in a Sorted Array of Unknown Size
    - 153. Find Minimum in Rotated Sorted Array
    - 74. Search a 2D Matrix(非二分但常考)
    - Search for a Range: 34. Find First and Last Position of Element in Sorted Array
    - Maximum Number in Mountain Sequence: 852. Peak Index in a Mountain Array

- 第三境界：二分位置 之 Half half

> 并无法找到一个条件，形成 OOXX 的模型,但可以根据判断，保留下有解的那一半或者去掉无解的一半

    - 162. Find Peak Element
    - 33. Search in Rotated Sorted Array(会了这道题，才敢说自己会二分法)

- 第四境界：二分答案 Binary Search on Result

> 往往没有给你一个数组让你二分，而且题目压根看不出来是个二分法可以做的题，同样是找到满足某个条件的最大或者最小值

    - 69. Sqrt(x)
    - 183L. Wood Cut
    - 437L. Copy Books


> EG(以实际为准)

```python
def binaryclassical(nums, target):
    if not nums or len(nums) == 0:
        return -1
    lo, hi = 0, len(nums)-1
    while lo + 1 < hi:
        # 剩下两个数的时候停止
        mid = lo + (hi-lo)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            lo = mid
        else:
            hi = mid
    if nums[lo] == target:
        return lo
    if nums[hi] == target:
        return hi
    return -1


res = binaryclassical([2, 3, 5, 8, 13, 21, 34, 55, 89], 89)
print(res)
```


### 34. Find First and Last Position of Element in Sorted Array

还算顺利

[lo + 1 < hi 避免死循环](https://blog.csdn.net/KID0031/article/details/100080420)

start和end相邻时，mid会偏左，这样start不会移动位置，而二分法每次是要减一半的

### 278. First Bad Version

用`lo + 1 < hi`和`lo = mid + 1`,`hi = mid - 1`在3，2出错，改为`lo = mid`,`hi = mid`。也就是说这还没明白。

### 658. Find K Closest Elements

错成shit

### 702.Search in a Sorted Array of Unknown Size

lock

课件没声音啊，所以这几道题看了以下几个网页笔记：

[九章算法笔记 2.Binary Search](https://stomachache007.wordpress.com/2017/03/11/%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95%E7%AC%94%E8%AE%B0-2-binary-search/)
[【九章算法基础班】二分法 - Siyao's Blog](https://marian5211.github.io/2017/12/07/%E3%80%90%E4%B9%9D%E7%AB%A0%E7%AE%97%E6%B3%95%E5%9F%BA%E7%A1%80%E7%8F%AD%E3%80%91%E4%BA%8C%E5%88%86%E6%B3%95/)
[九章算法系列（#2 Binary Search）-课堂笔记](https://www.cnblogs.com/Raising-Sun/p/5747072.html)

### 153. Find Minimum in Rotated Sorted Array

每次都和末尾元素或者right元素比较，决定搜右半还是左半。

### 74. Search a 2D Matrix

先二分找到行再在行内二分；或将矩阵看作一个长列表直接二分。

### 852. Peak Index in a Mountain Array

easy，根据指针和左右邻居的大小决定移动。

### 162. Find Peak Element

类似852

### 33. Search in Rotated Sorted Array

先找到最小，再二分，或者直接二分

###  69. Sqrt(x)

可用二分

###  183L. Wood Cut

Lintcode

###  437L. Copy Books

Lintcode