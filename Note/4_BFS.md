# 大纲

• 二叉树上的宽搜 BFS in Binary Tree
• 图上的宽搜 BFS in Graph
    • 拓扑排序 Topological Sorting
• 棋盘上的宽搜 BFS

# 什么时候应该使用BFS？

**图的遍历 Traversal in Graph**

• 层级遍历 Level Order Traversal

    - 102. Binary Tree Level Order Traversal

    - 107. Binary Tree Level Order Traversal II

    - 103. Binary Tree Zigzag Level Order Traversal

    - 297. Serialize and Deserialize Binary Tree

• 由点及面 Connected Component

    - 261. Graph Valid Tree

    - 133. Clone Graph

• 拓扑排序 Topological Sorting
> 一般用BFS

    - 207. Course Schedule

    - 210. Course Schedule II

    - 444. Sequence Reconstruction

**最短路径 Shortest Path in Simple Graph**

    - 611. Knight Shortest Path(lintcode lock)

    - 573. Build Post Office II

• 仅限简单图求最短路径

• 即，图中每条边长度都是1，且没有方向


> 如果题目问最短路，除了BFS还能是什么算法？

- 有很多，但是在北美你会BFS就行(or 动态规划)，迪杰斯特拉，北美不用掌握

> 如果问最长呢？

- 一定不能BFS
- DFS，全找一遍看最长；或者动态规划


## 二叉树上的宽搜 BFS in Binary Tree

### 102. Binary Tree Level Order Traversal

### 107. Binary Tree Level Order Traversal II

### 103. Binary Tree Zigzag Level Order Traversal

- **三道层序遍历，复习了下queue的使用**


> 图的遍历（层级遍历）

> 注：树是图的一种特殊形态，树属于图

### BFS Key Points

**使用队列作为主要的数据结构 Queue**

**是否需要实现分层？**

> i.e. [3,9,20,null,null,15,7]是输出[[3], [9,20], [15,7]]还是[3,9,20,15,7]

需要分层的算法比不需要分层的算法多一个循环

**size = q.qsize()**

### 时间复杂度

- **二叉树的问题基本都是O(n)**

- 不要只看for * while，看进出数据结构几次
    - head = q.get()， 每个点只进出一次，所以O(n)
- 空间复杂度，看queue里同时存多少个点，最坏情况O(n)


### 297. Serialize and Deserialize Binary Tree

序列化算法设计时需考虑因素：压缩率&可读性


## 图上的宽搜 BFS in Graph

> 和树的最大不同是，图中存在环，存在环意味着，同一个节点可能重复进入队列

用hashset或hashmap解决

### 261. Graph Valid Tree

> 图的遍历（由点及面）

树需要满足：

1. n-1条边

2. 连通性

#### BFS时间复杂度

图 Graph
N个点，M条边
M最大是 O(N^2) 的级别
图上BFS时间复杂度 = O(N+M)
- 说是O(M)问题也不大，因为M一般都比N大
所以最坏情况可能是 O(N^2)
一般不说最坏情况

#### BFS空间复杂度

O(n):把每个点往queue里放一次

#### BFS要点

1. BFS 在图上：hash + queue
2. BFS 在树上：while + for循环体

**能够用 BFS 解决的问题，一定不要用 DFS 去做！**

BFS没有递归，比较简单。

*通过这道题还要了解到图的表示方式*

### 133. Clone Graph
> 图的遍历（由点及面）

1. node -> nodes
2. nodes -> new nodes
3. edges -> new edges

在写程序时，能分开写不要合起写，不要一边clone nodes，一边clone edges

### 618. Search Graph Nodes(Lintcode LOCK)

和上一道比就是多了个判断。

如果要找所有最近的value=target的点，才需要分层。


## 拓扑排序

在一个有向图中，对所有的节点进行排序，要求没有一个节点指向它前面的节点。

先统计所有节点的入度，对于入度为0的节点就可以分离出来，然后把这个节点指向的节点的入度减一。

一直做改操作，直到所有的节点都被分离出来。

如果最后不存在入度为0的节点，那就说明有环，不存在拓扑排序，也就是很多题目的无解的情况。


### 127. Topological Sorting(Lintcode)

> 能用DFS，但是最好用BFS

就是个宽度优先搜索，但是有条件，入度为零才可以进入。

先存好每个点初始入度，然后找到入度为0的，然后bfs，每次把遍历过的点的邻居的入度减一。

**几乎所有公司都会有一道拓扑排序，一定要会。**

只用hashmap存入度就行，不需要set

1. 创建入度信息

2. 找初始点

3. BFS

### 207. Course Schedule

**比127L多一点用map初始化图**

### 210. Course Schedule II

**和207不同在于现在要返回拓扑排序后的结果**

### 444. Sequence Reconstruction [LOCK]
> [605. Sequence Reconstruction](https://www.lintcode.com/problem/sequence-reconstruction/description)


## 矩阵中的宽度优先搜索

### 时间复杂度

矩阵 Matrix：N行M列
N * M个点，N * M * 2 条边（每个点上下左右4条边，每条边被2个点共享）。
矩阵中BFS时间复杂度 = O(N * M)

### 200. Number of Islands
> 图的遍历（由点及面）

和图上不同在于找邻居时要用四个方向去判断。

### 598. Zombie in Matrix

不要直接判断是否等于0，1，2。而是用常量。这是一个代码风格的问题。

# 994橘子那道题，又是把`=`写成`==`，找了十分钟错误才找到！！！

```python
grid[nx][ny] == self.rotten
```

就这行！！！！！

## 简单图最短路径

### 611. Knight Shortest Path(lintcode lock)

0代表可到达，1代表不可。判断是否可从初始点到达终点。

```python
class Solution:
    def shortestPath(self, grid, soure, destinaiton):
        if not grid or not grid[0]:
            return -1
        derX = [1,1,2,2,-1,-1,-2,-2]
        derY = [2,-2,1,-1,2,-2,1,-1]
        import queue
        q = queue.Queue()
        q.put((soure[0],soure[1]))
        res = 0
        while not q.empty():
            res += 1
            size = q.qsize()
            for i in range(size):
                step = q.get()
                for j in range(8):
                    nx = step[0]+derX[j]
                    ny = step[1]+derY[j]
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] == 0:
                        q.put((nx,ny))
                        if [nx, ny] == destinaiton:
                            return res
        return -1
```

> 也许多加一个走过的置1？


### 573. Build Post Office II


# 总结

## 能用 BFS 的一定不要用 DFS（除非面试官特别要求）

## BFS 的两个使用条件
- 图的遍历（由点及面，层级遍历）

- 简单图最短路径

## 是否需要层级遍历
> size = queue.qsize()

第几天这种就需要层级遍历

## 拓扑排序必须掌握！

**几乎所有公司都会有一道拓扑排序，一定要会。**

## 坐标变换数组

- deltaX, deltaY

- inBound