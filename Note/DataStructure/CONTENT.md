# Note About Data Structure and Algorithm <!-- omit in toc -->

![](https://img.shields.io/badge/CurrentStatus-HardWorking-red)

---

Table of contents

- [Data Structure](#data-structure)

    - [String](#string)

    - [ArrayList](#arraylist)

    - [LinkedList](#linkedlist)

    - [HashMap](#hashmap)

    - [HashSet](#hashset)

    - [Queue](#queue)

    - [Stack](#stack)

    - [Heap](#heap)

    - [Tree](#tree)

- [Sort](#sort)

    - [Bubble Sort](#bubble-sort)
    
    - [Selection Sort](#selection-sort)
    
    - [Insertion Sort](#insertion-sort)
    
    - [Shell Sort](#shell-sort)
    
    - [Merge Sort](#merge-sort)
    
    - [Quick Sort](#quick-sort)
    
    - [Heap Sort](#heap-sort)
    
    - [Bucket Sort](#bucket-sort)
    
    - [Counting Sort](#counting-sort)
    
    - [Radix Sort](#radix-sort)

- [Algorithm](#algorithm)

    - [Recursion](#recursion)

    - [Divide and Conquer](#divide-and-conquer)

    - [Dynamic Programming](#dynamic-programming)

    - [Greedy Algorithm](#greedy-algorithm)

    - [Backtracking](#backtracking)

    - [Branch and Bound](#branch-and-bound)


---


# Data Structure

时间复杂度参考以下两个链接：

[Big O Cheat Sheet，但是好多都不对啊](https://www.bigocheatsheet.com/)

[Big O various data structures，基于JAVA，比上一个靠谱](https://stackoverflow.com/questions/7294634/what-are-the-time-complexities-of-various-data-structures)

## String

### Definition

String literals in python are surrounded by either single quotation marks, or double quotation marks.

### Implement

`str()`

### Operation

Python中字符串常用的方法：

```python
s0 = str()

s1 = ''

s2 = "Lexington"

length = len(s2)

s2[-3:] # ton

s2[5:8] # gto

s3 = s2[:3] # Lex

s2[::-1] # notgnixeL

s2[:-3] # Lexing

s3 += 'us' # Lexus

# list in python is same as ArrayList in java
s3list = list(s3) # ['L', 'e', 'x', 'u', 's']

s2.index('e')  # return 1, if not found, throw ValueError

s2.find('x') # return 2, if not found, return -1
```

### Time Complexity

### Related


## ArrayList

### Definition

A list is a collection which is ordered and changeable. Allows duplicate members. In Python lists are written with square brackets.

### Implement

`list()`

See comparison between List, Tuple, Set and Dictionary [HERE](https://github.com/Vida42/Leetcode/tree/master/Note/DataStructure/HighFreqPyOp.md).

### Operation

```python
# 使用list.count()，可以得到每一个元素，在list中出现的次数
b = ['do','you','me','you']
z = b.count(b[1])

a.join(b)
a = 'like'
b = ['do','you','me','you']
c = 'IU'
print(a.join(b))
# >>> 'dolikeyoulikemelikeyou'
print(a.join(c))
# >>> 'IlikeU'

# int转str
d = list(map(str,[1,2,3,4,5,6,7,8]))
# int转str
d2 = ''.join([str(i) for i in [1,2,3,4]])


# Python List四种删除元素的方法：

# According to index: del, pop
# According to value: remove

li = [1,2,2,3,2,4]

# 1. 使用del删除指定元素
# del removes the item at a specific index

del li[4]
# >>> li = [1,2,2,3,4]

# 2. 使用list方法pop删除元素
# pop removes the item at a specific index and returns it.

li.pop(4)
# >>> 2
# >>> li = [1,2,2,3,4]

# 3. 使用list方法remove删除指定值的元素
# remove removes the first matching value

li.remove(2)
# >>> li = [1,2,3,2,4]

li.remove(2)
# >>> li = [1,3,2,4]

# 4. 使用切片删除元素

li = li[:3]+li[4:]
# >>> li = [1,2,2,2,4]
```

### Time Complexity

<table>
<tr>
    <td><b>Name</b></td>
    <td><b>Access/Search</b></td>
    <td><b>Insert</b></td>
    <td><b>Delete</b></td>
</tr>

<tr>
    <td> Array </td>
    <td> by index : O(1) </br> by value : O(n) </td>
    <td> tail : O(1) </br> other : O(n) </td>
    <td> O(n) </td>
</tr>

<tr>
    <td> LinkedList </td>
    <td> head/tail : O(1) </br> other : O(n) </td>
    <td> head/tail : O(1) </br> other : O(n) </td>
    <td> head/tail : O(1) </br> other : O(n) </td>
</tr>
</table>

[Big O of various operations in current CPython，python官方文档](https://wiki.python.org/moin/TimeComplexity)

[What is the cost/ complexity of insert in list at some location?](https://stackoverflow.com/questions/27073596/what-is-the-cost-complexity-of-insert-in-list-at-some-location)

For Array in Python, insert at tail: append()
access by index: Get Item
access by value: Pop intermediate

Linked List, just O(n). O(1) in corner case.

### Related


## LinkedList

### Definition



### Implement


See [here](https://github.com/Vida42/Leetcode/blob/master/Note/DataStructure/LinkedList.py)

### Operation



### Time Complexity


[Performance Analysis of ArrayList and LinkedList in Java，有分析各个情况下该用哪种](https://dzone.com/articles/performance-analysis-of-arraylist-and-linkedlist-i)

### Related



## HashMap

### Definition

Map 是一种关联数组的数据结构，也常被称为字典或键值对。

Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

### Implement

`dict()` in Python

### Operation

```python
# three ways to construct a couting dict
nums = 'here' 

dic = dict()
for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dic = {} 
for c in nums: 
    dic[c] = (dic[c] + 1) if (c in dic) else (1)

dic = dict()
for i in nums:
    dic[i] = dic.get(i, 0) + 1

# difference between dic.get() and dic[key]: latter would throw KeyError when no such a key exists.

# Get the value of a key, if not exist return default
dict.get(key, default=None)

# returns keys of a dictionary
dic.keys()

# return values of a dictionary
dic.values()

# return (keys,values) tuple of a dict
dic.items()

# removes the item with the specified key name, return value
dic.pop(key)
```

### Time Complexity

**In Python, most dict operations(like `get`, `isin`, `delete` are O(1)**, `copy`) are O(n).

According to *[Time complexity of accessing a Python dict](https://stackoverflow.com/questions/1963507/time-complexity-of-accessing-a-python-dict)* : The python dict is a hashmap, its worst case is therefore O(n) if the hash function is bad and results in a lot of collisions. However that is a very rare case where every item added has the same hash and so is added to the same chain which for a major Python.

[Big O for List, Dictionaries, Sets](https://www.geeksforgeeks.org/complexity-cheat-sheet-for-python-operations/)

[List, Set, Dic in Python](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

### Related

## HashSet

### Definition

A set is a collection which is unordered, unchangeable and unindexed. In Python, sets are written with curly brackets.

### Implement

`set()`

### Operation

```python
# Add an item to a set
add()
# To remove an item in a set
remove()
# union() method returns a new set with all items from both sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
```

### Time Complexity

Sets have many more operations that are O(1) compared with lists and tuples. eg: `is in`, `add`, `remove`. `copy` has O(n).

### Related


## Queue

### Definition

- 队列是一个有序列表，可以用数组或者是链表来实现。

- 遵循先进先出的原则。即：先存入队列的数据，要先取出。后存入的要后取出。

### Implement

#### 链表实现
- [See Here](https://github.com/Vida42/Leetcode/blob/master/Note/DataStructure/LinkedQueue.py)

#### 简单数组实现：

```python
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
queue[0] # return 2 examine the first element
```

#### 高效实现：

- `queue.Queue` or `collections.deque`

`queue.Queue` and `collections.deque` serve different purposes. queue.Queue is intended for allowing different threads to communicate using queued messages/data, whereas `collections.deque` is simply intended as a data structure.

> [queue.Queue vs. collections.deque](https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque)

### Operation

<table>
<tr>
    <td><b>Function</b></td>
    <td><b>collections.deque</b></td>
    <td><b>queue.Queue</b></td>
</tr>
<tr>
    <td>enqueue left</td>
    <td>dq.appendleft()</td>
    <td> / </td>
</tr>
<tr>
    <td>enqueue right</td>
    <td>dq.append()</td>
    <td>queue.put()</td>
</tr>
<tr>
    <td>dequeue left</td>
    <td>dq.popleft()</td>
    <td> / </td>
</tr>
<tr>
    <td>dequeue right</td>
    <td>dq.pop()</td>
    <td>queue.get()</td>
</tr>
<tr>
    <td>peek left</td>
    <td>dq[0]</td>
    <td> / </td>
</tr>
<tr>
    <td>peek right</td>
    <td>dq[-1]</td>
    <td> / </td>
</tr>
<tr>
    <td>size</td>
    <td>len(dq)</td>
    <td>queue.qsize()</td>
</tr>
</table>

Otherwise, Quque.queue has queue.empty() and queue.full()

> [python queue get size, use qsize() or len()?](https://stackoverflow.com/questions/20647274/python-queue-get-size-use-qsize-or-len)

### Time Complexity

<table>
<tr>
    <td><b>Name</b></td>
    <td><b>Append</b></td>
    <td><b>Pop</b></td>
    <td><b>Size</b></td>
    <td><b>Copy</b></td>
    <td><b>Search</b></td>
</tr>

<tr>
    <td> Queue </td>
    <td> O(1) </td>
    <td> O(1) </td>
    <td> O(1) </td>
    <td> O(n) </td>
    <td> O(n) </td>
</tr>
</table>

以上特性皆显然。No matter Average Case or Amortized Worst Case

### Related

## Stack

### Definition

栈是一种 LIFO(Last In First Out) 的数据结构，常用方法有添加元素，取栈顶元素，弹出栈顶元素，判断栈是否为空。

### Implement

#### 链表实现
- [See Here](https://github.com/Vida42/Leetcode/blob/master/Note/DataStructure/LinkedStack.py)

#### 简单数组实现：

可以用list简单实现

#### 高效实现：

- `collections.deque`

### Operation

见上

### Time Complexity

<table>
<tr>
    <td><b>Name</b></td>
    <td><b>Push</b></td>
    <td><b>Pop</b></td>
    <td><b>Top</b></td>
    <td><b>Size</b></td>
    <td><b>Copy</b></td>
    <td><b>Search</b></td>
</tr>

<tr>
    <td> Stack </td>
    <td> O(1) </td>
    <td> O(1) </td>
    <td> O(1) </td>
    <td> O(1) </td>
    <td> O(n) </td>
    <td> O(n) </td>
</tr>
</table>

For all the standard stack operations (push, pop, isEmpty, size), the worst-case run-time complexity can be O(1).([Notes on Stacks](http://pages.cs.wisc.edu/~siff/CS367/Notes/stacks.html))

### Related


## Heap

### Definition

一般情况下，堆通常指的是**二叉堆**，**二叉堆**是一个近似**完全二叉树**的数据结构，但由于对二叉树平衡及插入/删除操作较为麻烦，二叉堆实际上使用数组来实现。即物理结构为数组，逻辑结构为完全二叉树。子结点的键值或索引总是小于（或者大于）它的父节点，且每个节点的左右子树又是一个**二叉堆**(大根堆或者小根堆)。根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。常被用作实现**优先队列**。

**优先队列**，名字里带队列，形式上是一种队列的形式(数组)，但其实和队列的概念无关，是一种独立的抽象数据类型，可以用二叉堆这种特殊的树结构实现(see [HERE](https://github.com/Vida42/Leetcode/blob/master/Note/2019begins/Heap.md))。

在索引从0开始的数组中：

- 父节点 i 的左子节点在位置(2 * i+1)

- 父节点 i 的右子节点在位置(2 * i+2)

- 子节点 i 的父节点在位置floor((i-1)/2)

### Implement

`heapq` which maintains a `min heap`

### Operation

创建堆：将堆所有数据重新排序

堆调整：将堆的末端子节点作调整，使得子节点永远大于父节点

堆排序：移除位于第一个数据的根节点，并做堆调整的递归运算

```python

# To create a heap, use a list initialized to []
# or you can transform a populated list into a heap via function heapify().
heapq.heapify(x)

heapq.heappush(heap, item)

# Pop and return the smallest item from the heap
heapq.heappop(heap)

```

### Time Complexity

<table>
<tr>
    <td><b>Name</b></td>
    <td><b>Insert</b></td>
    <td><b>Find Min/Max</b></td>
    <td><b>Delete Min/Max</b></td>
    <td><b>Extract Min/Max</b></td>
    <td><b>Delete</b></td>
    <td><b>Search</b></td>
</tr>

<tr>
    <td> Heap/PriorityQueue </td>
    <td> O(log n) </td>
    <td> O(1) </td>
    <td> O(log n) </td>
    <td> O(log n) </td>
    <td> O(n) </td>
    <td> O(n) </td>
</tr>
</table>

`heapq` is a binary heap, with O(log n) `push` and O(log n) `pop`. See [here](https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library).

`push` means Insert; `pop` means Extract/Delete Min/Max, this requires rebuild heap, which is O(log n).

Delete and Search is O(n) because we will have to scan all the elements as they are not ordered like BST.

The big O of building a heap is O(n). See [here](https://stackoverflow.com/questions/9755721/how-can-building-a-heap-be-on-time-complexity).

heapify() actually takes linear time because the approach is different than calling heapq.push() N times.

九章提到PriorityQueue的delete是O(n)，但heap的也是logn。如果需要比O(n)小的删除操作，用TreeMap，支持各种操作皆为logn。

### Related

## Tree

### Definition

- 二叉树：每个结点最多有两个子树的树结构。

- 满二叉树：树中每个分支结点（非叶结点）都有两棵非空子树

> 这应该是full binary tree

![满二叉树](https://github.com/Vida42/Leetcode/blob/master/Pic/cap1.PNG)

- 完全二叉树(complete binary tree)：对于一个树高为h的二叉树，如果其第0层至第h-1层的节点都满。如果最下面一层节点不满，则所有的节点在左边的连续排列，空位都在右边。这样的二叉树就是一棵完全二叉树。

![完全二叉树](https://github.com/Vida42/Leetcode/blob/master/Pic/cap2.PNG)

- perfect binary tree: Every node except the leaf nodes have two children and every level (last level too) is completely filled

![](https://github.com/Vida42/Leetcode/blob/master/Pic/cap3.PNG)


[Source](http://courses.cs.vt.edu/~cs3114/Summer14/Notes/T03_BinaryTreeTheorems.pdf)

如果根节点算第一层：

- 二叉树的第i层至多有 2^{i-1}个结点

- 深度为k的二叉树至多有 2^k-1个结点

### Implement

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

### Operation

> 从二叉树的根节点出发，节点的遍历分为三个主要步骤：对当前节点进行操作（称为“访问”节点）、遍历左边子节点、遍历右边子节点。访问节点顺序的不同也就形成了不同的遍历方式。需要注意的是树的遍历通常使用递归的方法进行理解和实现。按照访问元素的前后顺序，遍历方式可划分为如下几种：

* 深度优先
    * 1. 先序(pre-order)：根左右
    * 2. 中序(in-order)：左根右
    * 3. 后序(post-order)：左右根
* 广度优先
    * 层序(level-order)

> 对树相关的题进行复杂度分析时可统计对每个节点被访问的次数，进而求得总的时间复杂度。


满足以下性质的二叉树是一颗二叉搜索树：

* 若左子树不为空，左子树上所有节点的值都小于根节点的值；
* 若右子树不为空，右子树上所有节点的值都大于根节点的值；
* 它的左右子树也分别是二叉搜索树。

使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。


### Time Complexity

Binary Search Tree:

Insert, delete and search:

Average case: O(log n), Worst Case: O(n)

[Binary tree has worst case complexity of O(n). In general, time complexity is O(h) where h is height of BST](https://www.geeksforgeeks.org/complexity-different-operations-binary-tree-binary-search-tree-avl-tree/).

Another [example](http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/bin-tree.html) explains the relationship between height and nodes of a binary tree.

### Related

[Some exercises](https://github.com/Vida42/Leetcode/tree/master/Note/DataStructure/TreeExercise.md)

# Sort

稳定性：保证排序前2个相等的数其在序列的前后位置顺序和排序后它们两个的前后位置顺序相同。如果Ai = Aj，Ai原来在位置前，排序后Ai还是要在Aj位置前。

以下所有排序实现均默认从小到大。

<table>
<tr>
    <td><b>Type</b></td>
    <td><b>Name</b></td>
    <td><b>Best</b></td>
    <td><b>Average</b></td>
    <td><b>Worst</b></td>
    <td><b>Memory</b></td>
    <td><b>Stable</b></td>
    <td><b>Method</b></td>
    <td><b>Other Notes</b></td>
</tr>

<tr>
    <td rowspan="7"> <a href=""> Comparison Sorts </a></td>
    <td> Quick Sort </td>
    <td> nlogn </td>
    <td> nlogn </td>
    <td> n^2 </td>
    <td> logn </td>
    <td>No</td>
    <td>Partitioning</td>
    <td> Quicksort is usually done in-place with O(log n) stack space. </td>
</tr>
<tr>
    <td> Merge Sort </td>
    <td> nlogn </td>
    <td> nlogn </td>
    <td> nlogn </td>
    <td> n </td>
    <td>Yes</td>
    <td>Merging</td>
    <td> Highly parallelizable (up to O(log n) using the Three Hungarians' Algorithm). </td>
</tr>
<tr>
    <td> Selection Sort </td>
    <td> n^2 </td>
    <td> n^2 </td>
    <td> n^2 </td>
    <td> 1 </td>
    <td>No</td>
    <td>Selection</td>
    <td> Stable with O(n) extra space or when using linked lists. </td>
</tr>
<tr>
    <td> Heap Sort </td>
    <td> nlogn </td>
    <td> nlogn </td>
    <td> nlogn </td>
    <td> 1 </td>
    <td>No</td>
    <td>Selection</td>
    <td></td>
</tr>
<tr>
    <td> Insertion Sort </td>
    <td> n </td>
    <td> n^2 </td>
    <td> n^2 </td>
    <td> 1 </td>
    <td>Yes</td>
    <td>Insertion</td>
    <td> O(n + d), in the worst case over sequences that have d inversions. </td>
</tr>
<tr>
    <td> Shell Sort </td>
    <td> nlogn </td>
    <td> n^(4/3) </td>
    <td> n^(3/2) </td>
    <td> 1 </td>
    <td>No</td>
    <td>Insertion</td>
    <td> Small code size. </td>
</tr>
<tr>
    <td> Bubble Sort </td>
    <td> n </td>
    <td> n^2 </td>
    <td> n^2 </td>
    <td> 1 </td>
    <td>Yes</td>
    <td>Exchanging</td>
    <td> Tiny code size. </td>
</tr>
<tr>
    <td rowspan="3"> <a href=""> Non-comparison Sorts </a></td>
    <td> Bucket Sort </td>
    <td>  </td>
    <td> n + r </td>
    <td> n + r </td>
    <td> n + r </td>
    <td>Yes</td>
    <td> </td>
    <td> Assumes uniform distribution of elements from the domain in the array. </td>
</tr>
<tr>
    <td> Counting Sort </td>
    <td>  </td>
    <td> n + r </td>
    <td> n + r </td>
    <td> n + r </td>
    <td>Yes</td>
    <td> </td>
    <td> If r is O(n), then average time complexity is O(n) </td>
</tr>
<tr>
    <td> Radix Sort </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td>  </td>
    <td></td>
    <td>  </td>
    <td>  </td>
</tr>
<table>

## Bubble Sort

### Intro

重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

![](https://algorithm.yuanbin.me/shared-files/images/bubble_sort.gif)

### Step

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。

2. 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。

3. 针对所有的元素重复以上的步骤，除了最后一个。

4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

### Code

```python
def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j],arry[j-1]      #则交换两者
    return arry
```

### Complexity

尽管这个算法是最简单了解和实现的排序算法之一，但它对于包含大量的元素的数列排序是很没有效率的。

优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。

优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。

平均情况与最坏情况均为 O(n^2)，空间复杂度为 O(1).


## Selection Sort

### Intro

选择排序也是一种简单直观的排序算法。初始时在序列中找到最小元素，放到序列的起始位置作为已排序序列；然后，再从剩余未排序元素中继续寻找最小元素，放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

![](https://algorithm.yuanbin.me/shared-files/images/selection_sort.gif)

### Step

1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。

2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

3. 以此类推，直到所有元素均排序完毕。


### Code

```python
def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary
```

### Complexity

如果当前元素比一个元素小，而该小的元素又出现在一个和当前元素相等的元素后面，那么交换后稳定性就被破坏了。举个例子，[5, 8, 5, 2, 9]，我们知道第一遍选择第1个元素5会和2交换，那么原序列中2个5的相对前后顺序就被破坏了，所以选择排序不是一个稳定的排序算法。

注意选择排序与冒泡排序的区别：冒泡排序通过依次交换相邻两个顺序不合法的元素位置，从而将当前最小（大）元素放到合适的位置；而选择排序每遍历一次都记住了当前最小（大）元素的位置，最后仅需一次交换操作即可将其放到合适的位置。

表现最稳定的排序算法之一，因为无论什么数据进去都是O(n2)的时间复杂度，所以用到它的时候，数据规模越小越好。


## Insertion Sort

### Intro

插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

其类似于我们抓扑克牌，对于右手抓到的牌(对于未排序数据)，在左手已经排好序的手牌(已排序序列)中从后向前扫描，找到相应位置并插入。

![](http://wuchong.me/img/Insertion-sort-example-300px.gif)

### Step

1. 从第一个元素开始，该元素可以认为已经被排序

2. 取出下一个元素，在已经排序的元素序列中从后向前扫描

3. 如果被扫描的元素（已排序）大于新元素，将该元素后移一位

4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置

5. 将新元素插入到该位置后

6. 重复步骤2 - 5

### Code

```python
def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
            ary[index] = temp
    return ary
```

### Complexity

在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。


## Shell Sort

### Intro

希尔排序是基于插入排序的以下两点性质而提出改进方法的：

- 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率

- 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

### Step

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，这样可以让一个元素可以一次性地朝最终位置前进一大步，可以提升插入排序的性能。然后算法再取越来越小的步长进行排序，待整个序列中的记录"基本有序"时，进行最后一步（就是普通的插入排序）：对全体记录进行依次直接插入排序，到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）。

### Code

```python
# 此程序步长的选择是从n/2开始，每次再减半，直至为0。步长的选择直接决定了希尔排序的复杂度
def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary
```

### Complexity

希尔排序，也叫递减增量排序，是插入排序的一种更高效的改进版本。希尔排序是不稳定的排序算法，因为虽然一次插入排序是稳定的，不会改变相同元素的相对顺序，但在不同的插入排序过程中，相同的元素可能在各自的插入排序中移动，最后其稳定性就会被打乱。

比如序列：{ 3, 5, 10, 8, 7, 2, 8, 1, 20, 6 }，h=2时分成两个子序列 { 3, 10, 7, 8, 20 } 和  { 5, 8, 2, 1, 6 } ，未排序之前第二个子序列中的8在前面，现在对两个子序列进行插入排序，得到 { 3, 7, 8, 10, 20 } 和 { 1, 2, 5, 6, 8 } ，即 { 3, 1, 7, 2, 8, 5, 10, 6, 20, 8 } ，两个8的相对次序发生了改变。


## Merge Sort

### Intro

- 归并排序是采用分治法的一个非常典型的应用。`归并`排序的思想就是先`递归分解`数组，再`合并`数组。

- 排序和另一个非常重要的排序方法：快速排序非常相似，都是基于分治法的递归排序

![](http://wuchong.me/img/Merge-sort-example-300px.gif)

### Step

先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。然后合并排序相邻二个小组即可。

### Code

```python
def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
```

### Complexity

排序时间与输入无关，都是O(nlogn): 合并消耗O(n)，归并需要进行logn(以2为底)次，所以O(nlogn)。

**in-place??**


## Quick Sort

### Intro

核心：快排是一种采用分治思想的排序算法，大致分为三个步骤：定基准，划分区，递归调用。

![](http://wuchong.me/img/Quicksort-example.gif)

- 方法其实很简单：分别从初始序列“6 1 2 7 9 3 4 5 10 8”两端开始“探测”。先从右往左找一个小于6的数，再从左往右找一个大于6的数，然后交换他们。这里可以用两个变量i和j，分别指向序列最左边和最右边。我们为这两个变量起个好听的名字“哨兵i”和“哨兵j”。刚开始的时候让哨兵i指向序列的最左边（即i=1），指向数字6。让哨兵j指向序列的最右边（即=10），指向数字。
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218121956.png)
- 首先哨兵j开始出动。因为此处设置的基准数是最左边的数，所以需要让哨兵j先出动，这一点非常重要（请自己想一想为什么）。哨兵j一步一步地向左挪动（即j–），直到找到一个小于6的数停下来。接下来哨兵i再一步一步向右挪动（即i++），直到找到一个数大于6的数停下来。最后哨兵j停在了数字5面前，哨兵i停在了数字7面前。
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122030.png)
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122042.png)
- 现在交换哨兵i和哨兵j所指向的元素的值。交换之后的序列如下：
  `6 1 2 5 9 3 4 7 10 8`
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122148.png)
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122203.png)
- 到此，第一次交换结束。接下来开始哨兵j继续向左挪动（再友情提醒，每次必须是哨兵j先出发）。他发现了4（比基准数6要小，满足要求）之后停了下来。哨兵i也继续向右挪动的，他发现了9（比基准数6要大，满足要求）之后停了下来。此时再次进行交换，交换之后的序列如下：
  `6 1 2 5 4 3 9 7 10 8`
- 第二次交换结束，“探测”继续。哨兵j继续向左挪动，他发现了3（比基准数6要小，满足要求）之后又停了下来。哨兵i继续向右移动，糟啦！此时哨兵i和哨兵j相遇了，哨兵i和哨兵j都走到3面前。说明此时“探测”结束。我们将基准数6和3进行交换。交换之后的序列如下：
  `3 1 2 5 4 6 9 7 10 8`
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122258.png)
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122321.png)
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218122330.png)
- 到此第一轮“探测”真正结束。此时以基准数6为分界点，6左边的数都小于等于6，6右边的数都大于等于6。回顾一下刚才的过程，其实哨兵j的使命就是要找小于基准数的数，而哨兵i的使命就是要找大于基准数的数，直到i和j碰头为止。
- OK，解释完毕。现在基准数6已经归位，它正好处在序列的第6位。此时我们已经将原来的序列，以6为分界点拆分成了两个序列，左边的序列是“3 1 2 5 4”，右边的序列是“9 7 10 8”。接下来还需要分别处理这两个序列。因为6左边和右边的序列目前都还是很混乱的。不过不要紧，我们已经掌握了方法，接下来只要模拟刚才的方法分别处理6左边和右边的序列即可。现在先来处理6左边的序列现吧。
- 左边的序列是“3 1 2 5 4”。请将这个序列以3为基准数进行调整，使得3左边的数都小于等于3，3右边的数都大于等于3。好了开始动笔吧
- 如果你模拟的没有错，调整完毕之后的序列的顺序应该是：
  `2 1 3 5 4`  
- OK，现在3已经归位。接下来需要处理3左边的序列“2 1”和右边的序列“5 4”。对序列“2 1”以2为基准数进行调整，处理完毕之后的序列为“1 2”，到此2已经归位。序列“1”只有一个数，也不需要进行任何处理。至此我们对序列“2 1”已全部处理完毕，得到序列是“1 2”。序列“5 4”的处理也仿照此方法，最后得到的序列如下：
  `1 2 3 4 5 6 9 7 10 8`
- 对于序列“9 7 10 8”也模拟刚才的过程，直到不可拆分出新的子序列为止。最终将会得到这样的序列，如下
  `1 2 3 4 5 6 7 8 9 10`
- 到此，排序完全结束。细心的同学可能已经发现，快速排序的每一轮处理其实就是将这一轮的基准数归位，直到所有的数都归位为止，排序就结束了。
- ![](https://markpersonal.oss-us-east-1.aliyuncs.com/pic/20200218123926.png)
- 快速排序之所比较快，因为相比冒泡排序，每次交换是跳跃式的。每次排序的时候设置一个基准点，将小于等于基准点的数全部放到基准点的左边，将大于等于基准点的数全部放到基准点的右边。这样在每次交换的时候就不会像冒泡排序一样每次只能在相邻的数之间进行交换，交换的距离就大的多了。因此总的比较和交换次数就少了，速度自然就提高了。当然在最坏的情况下，仍可能是相邻的两个数进行了交换。因此快速排序的最差时间复杂度和冒泡排序是一样的都是O(N2)，它的平均时间复杂度为O(NlogN)。其实快速排序是基于一种叫做“二分”的思想。

### Step

1. 从数列中挑出一个元素作为基准数。

2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。

3. 再对左右区间递归执行第二步，直至各区间只有一个数。

### Code

```python
def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right : return ary
    key = ary[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while ary[rp] >= key and lp < rp :
            rp -= 1
        while ary[lp] <= key and lp < rp :
            lp += 1
        ary[lp],ary[rp] = ary[rp],ary[lp]
    ary[left],ary[lp] = ary[lp],ary[left]
    qsort(ary,left,lp-1)
    qsort(ary,rp+1,right)
    return ary
```

### Complexity

在最坏情况下，即数组本来就有序，复杂度O(n^2)。

事实上，快速排序通常明显比其他O(nlogn)算法更快，因为它的内部循环可以在大部分的架构上很有效率地被实现出来。

- 归并排序将数组分成两个子数组分别排序，并将有序的子数组归并以将整个数组排序。递归调用发生在处理整个数组之前。

- 快速排序将一个数组分成两个子数组并对这两个子数组独立地排序，两个子数组有序时整个数组也就有序了。递归调用发生在处理整个数组之后。


## Heap Sort

### Intro

堆排序是指利用堆这种数据结构所设计的一种选择排序算法。思路：首先用N个元素构造一个二叉堆，接着连续删除根结点，为了实现原地排序的功能，删除的时候不要直接输出元素，而是将根结点和数组尾部元素互换位置，这样就不需要使用而外的数组。

![](http://wuchong.me/img/Heapsort-example.gif)

### Step

1. 创建最大堆（Build_Max_Heap）：若数组下标范围为0 ~ n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆(单个节点)。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。

1. 堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。

3. 最大堆调整（Max_Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点

建堆时可以自顶向下，也可以采取自底向上，以下先采用自底向上的思路分析。我们可以将数组的后半部分节点想象为堆的最下面的那些节点，由于是单个节点，故显然满足二叉堆的定义，于是乎我们就可以从中间节点向上逐步构建二叉堆，每前进一步都保证其后的节点都是二叉堆，这样一来前进到第一个节点时整个数组就是一个二叉堆了。

### Code

```python
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary


#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break
```

### Complexity

建堆时间：O(n)，一次堆调整时间：O(logn)，排序遍历一遍：O(n)，综上时间复杂度：O(nlogn)

堆本质还是用数组实现，所以in-place，空间复杂度：O(1)

[10亿个数中找出最大的10000个数（top K问题）](https://blog.csdn.net/zyq522376829/article/details/47686867)

用堆排序，因为堆排序只需要k大小的空间。

先拿10000个数建最小堆，然后一次添加剩余元素，如果大于堆顶的数（10000中最小的），将这个数替换堆顶，并调整结构使之仍然是一个最小堆，这样，遍历完后，堆中的10000个数就是所需的最大的10000个。

建堆时间复杂度是O(m)，堆调整的时间复杂度是O(logm)。最终时间复杂度 = 1次建堆时间 + n次堆调整时间 = O(m+nlogm) = O(nlogm)（n为10亿，m为10000）



## Bucket Sort

### Intro



### Step



### Code



### Complexity

## Counting Sort

### Intro



### Step



### Code



### Complexity

## Radix Sort

### Intro



### Step



### Code



### Complexity


# Algorithm

## Recursion

## Divide and Conquer

## Dynamic Programming

## Greedy Algorithm

## Backtracking

## Branch and Bound

[牛皮的数据结构和算法可视化](https://visualgo.net/en)

[old school风的Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

[Sorting algorithm Wikipedia](https://en.wikipedia.org/wiki/Sorting_algorithm#Non-comparison_sorts)

[Basic Data Structure and Sorting and Algorithms by billryan](https://algorithm.yuanbin.me/zh-hans/part_i_basics/)

[经典排序算法总结与实现](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/)

[几种排序的文字性介绍](https://www.cnblogs.com/codingmylife/archive/2012/10/21/2732980.html)

[比较排序的详细介绍](https://blog.csdn.net/wuzhiwei549/article/details/80654836)
