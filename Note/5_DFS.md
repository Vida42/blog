# outline

- Recursion
- Combination
- Permutation
- Graph
- Non-Recursion
    - Iterator

## 什么时候使用 DFS？

碰到让你找所有方案的题，一定是DFS

90%DFS的题，要么是排列，要么是组合
> 排列组合是隐式图

1. 从面试的角度，面试官有时希望你写dfs来看你写递归

2. dfs省空间


## 组合搜索问题 Combination

问题模型：求出所有满足条件的“组合”。

判断条件：组合中的元素是顺序无关的。

### 时间复杂度：与 2^n 相关。

DFS时间复杂度不太好算，如果问道，就假设树的节点有S个，O(S * n)

### 78. Subsets

这一系列题目记得先sort

O(n * 2^n)

一共2^n个节点，每个节点上一个循环，操作n次

或者：O(答案个数 * 构造每个答案的时间)

#### 递归三要素

- 递归的定义
- 递归的拆解
- 递归的出口

### 90. Subsets II

这次nums内有重复值，但输出不要重复

### 39. Combination Sum

与78相比：

1. 多了个限制条件

2. 可重复选择，所以结果集也有重复

O(潜在答案个数 * 构造每个答案的时间)

假设答案有S个，O(S * n)

### 40. Combination Sum II

与78相比：

1. 多了个限制条件

2. 不可重复选择，但数字有重复


## 排列搜索问题 Permutation

这种问题里不需要知道上一个选的是谁，而要知道选没选过。没选过就可以选。（1,2,3 is diff from 1,3,2）

### 时间复杂度：与 n! 相关。

### 46. Permutations

### 47. Permutations II

### 51. N-Queens

### 127. Word Ladder

先bfs记下所有点到终点的距离，再dfs求解

126. Word Ladder II
hard

//stack, no recursion
> 没什么通用性，只解决具体的问题…

必背* 6

二进制，记住subset那道题用二进制怎么做就好


394. Decode String(Expression Expand)

341. Flatten Nested List Iterator

栈相关必练

155. Min Stack
Easy

84. Largest Rectangle in Histogram
Hard

232. Implement Queue using Stacks
Easy


### 总结

什么时候用 DFS？
- 求所有方案时
怎么解决DFS？
- 不是排列就是组合
复杂度怎么算？
- O(答案个数 * 构造每个答案的时间复杂度)
非递归怎么办？
- 必“背”程序