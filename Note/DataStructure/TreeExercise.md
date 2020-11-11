#### 1. 对称的二叉树

以下判断二叉树对称的代码等价：

```python
    def compare(self, left, right):
        if left == None:
            return right == None
        if right == None:
            return False
        if left.val != right.val:
            return False
        return self.compare(left.right, right.left) and self.compare(left.left, right.right)

 
    def compare(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            return self.compare(left.left, right.right) and self.compare(left.right, right.left):
        return False
```


#### 2. 二叉树的下一个结点

> 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


1. 二叉树为空，则返回空；

2. 节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；

3. 节点不是根节点。如果该节点是其父节点的左孩子，则返回父节点；否则继续向上遍历其父节点的父节点，重复之前的判断，返回结果。代码如下：


#### 3. 二叉搜索树的第k个结点

二叉搜索树中序遍历返回有序数组。

#### 4. 把二叉树打印成多行

层次遍历：

访问根节点，并将根节点入队。
当队列不空的时候，重复以下操作。
1、弹出一个元素。作为当前的根节点。
2、如果根节点有左孩子，访问左孩子，并将左孩子入队。
3、如果根节点有右孩子，访问右孩子，并将右孩子入队。


#### 5. 按之字形顺序打印二叉树

一开始的思路是在层次遍历上直接加reverse，但是看到讨论区有人说：

> 大家的实现很多都是将每层的数据存进ArrayList中，偶数层时进行reverse操作，
> 在海量数据时，这样效率太低了。
> （我有一次面试，算法考的就是之字形打印二叉树，用了reverse，
> 直接被鄙视了，面试官说海量数据时效率根本就不行。）

我还是先这么着了。leetcode上还有人用BFS。**之后再看**。

#### 6. 数据流中的中位数

做法就是用一个大顶堆和一个小顶堆，维持大顶堆的数都小于等于小顶堆的数，且两者的个数相等或差1。平均数就在两个堆顶的数之中。

python的heapq是最小堆

两个参考之后再看，[一个是用heapq](https://leetcode.com/problems/find-median-from-data-stream/discuss/74158/Python-O(lgn)-using-two-heapq-data-sturctures)；[一个是夜小楼Dream自己实现，这个牛逼今天没看随后细看](https://www.nowcoder.com/questionTerminal/9be0172896bd43948f8a32fb954e1be1)

#### 7. 序列化二叉树

不想做了……

#### 8. 二叉树的深度

层次遍历，做了就忘？？

#### 9. 平衡二叉树

又不想做了……从上往下和从下往上回头看






https://github.com/Vida42/Leetcode/blob/master/Warehouse/001._Two_Sum.md
https://github.com/Vida42/Leetcode/blob/master/Warehouse/002._Add_Two_Numbers.md

leetcode 84
https://blog.csdn.net/weixin_42001089/article/details/84203651

'''
https://www.geeksforgeeks.org/split-array-three-equal-sum-subarrays/
https://www.geeksforgeeks.org/number-of-ones-in-the-smallest-repunit/
https://www.geeksforgeeks.org/count-pairs-array-whose-sum-divisible-4/
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem
'''
