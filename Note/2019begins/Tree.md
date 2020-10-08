> 树

## 概念

* 二叉树：每个结点最多有两个子树的树结构。
* 满二叉树：树中每个分支结点（非叶结点）都有两棵非空子树


<p align="center">
    <img src="https://github.com/Vida42/Leetcode/blob/master/Pic/cap1.PNG" alt="Sample"  width="256" height="128">
    <p align="center">
        <em>满二叉树</em>
    </p>
</p>




* 完全二叉树：对于一个树高为h的二叉树，如果其第0层至第h-1层的节点都满。如果最下面一层节点不满，则所有的节点在左边的连续排列，空位都在右边。这样的二叉树就是一棵完全二叉树。

<p align="center">
    <img src="https://github.com/Vida42/Leetcode/blob/master/Pic/cap2.PNG" alt="Sample"  width="256" height="128">
    <p align="center">
        <em>两棵完全二叉树</em>
    </p>
</p>


## 树的遍历

> 从二叉树的根节点出发，节点的遍历分为三个主要步骤：对当前节点进行操作（称为“访问”节点）、遍历左边子节点、遍历右边子节点。访问节点顺序的不同也就形成了不同的遍历方式。需要注意的是树的遍历通常使用递归的方法进行理解和实现。按照访问元素的前后顺序，遍历方式可划分为如下几种：
* 深度优先
* 1. 先序(pre-order)：根左右
* 2. 中序(in-order)：左根右
* 3. 后序(post-order)：左右根
* 广度优先
* * 层序(level-order)

> 对树相关的题进行复杂度分析时可统计对每个节点被访问的次数，进而求得总的时间复杂度。


## Binary Search Tree - 二叉搜索树

满足以下性质的二叉树：

* 若左子树不为空，左子树上所有节点的值都小于根节点的值；
* 若右子树不为空，右子树上所有节点的值都大于根节点的值；
* 它的左右子树也分别是二叉搜索树。

使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。


[0][完全二叉树基本知识](https://www.jianshu.com/p/a47d6ed886c8)


## Tree：11 / 47

|     |     |     |     |  基础/4  |
| --- | --- | --- | --- | --- |
|Medium|144|  Binary Tree Preorder Traversal |preorder|
|Medium|94    |Binary Tree Inorder Traversal  |Inorder|
|Hard|145|  Binary Tree Postorder Traversal |postorder|
|Medium|102|  Binary Tree Level Order Traversal   |DFS + BFS|√|
|     |     |     |     |  **preorder/9**  |
|Easy|100| Same Tree |preorder|√|
|Easy|101| Symmetric Tree |preorder|√|
|Easy|226| Invert Binary Tree |preorder + BFS|√|
|Easy|257| Binary Tree Paths |preorder|√|
|Easy|112| Path Sum |preorder|√|
|Medium|113| Path Sum II |preorder|
|Medium|129| Sum Root to Leaf Numbers |preorder|
|Medium|298| Binary Tree Longest Consecutive Sequence |preorder|
|Easy|111| Minimum Depth of Binary Tree |preorder|√|
|     |     |     |     |  **Postorder/6**  |
|Easy|104| Maximum Depth of Binary Tree |postorder|√|
|Easy|110| Balanced Binary Tree |postorder|-[x]|
|Hard|124| Binary Tree Maximum Path Sum |postorder|
|Medium|250| Count Univalue Subtrees |postorder|
|Medium|366| Find Leaves of Binary Tree |postorder|
|Medium|337| House Robber III |postorder + preorder|
|     |     |     |     |  **BFS/3**  |
|Easy|107|  Binary Tree Level Order Traversal II    |BFS|√|
|Medium|103|  Binary Tree Zigzag Level Order Traversal    |BFS|
|Medium|199|  Binary Tree Right Side View |BFS + preorder|
|     |     |     |     |  **BST/12**  |
|Medium|98    |Validate Binary Search Tree    |preorder|
|Medium|235|  Lowest Common Ancestor of a Binary Search Tree  |preorder|
|Medium|236|  Lowest Common Ancestor of a Binary Tree |postorder|
|Easy|108|  Convert Sorted Array to Binary Search Tree  |binary search|√|
|Medium|109|  Convert Sorted List to Binary Search Tree   |binary search|√|
|Medium|173|  Binary Search Tree Iterator |inorder|
|Medium|230|  Kth Smallest Element in a BST   |inorder|
|Medium|297|  Serialize and Deserialize Binary Tree   |BFS|
|Medium|285|  Inorder Successor in BST    |inorder|
|Easy|270|  Closest Binary Search Tree Value    |preorder|-[x]|
|Hard|272|  Closest Binary Search Tree Value II |inorder|
|Hard|99    |Recover Binary Search Tree |inorder|
|     |     |     |     |  **重要程度/13**  |
|Medium|156|  Binary Tree Upside Down |很少考|
|Medium|114|  Flatten Binary Tree to Linked List  |很少考|
|Medium|255|  Verify preorder Sequence in Binary Search Tree |很少考|
|Medium|333|  Largest BST Subtree |很少考|
|Medium|222|  Count Complete Tree Nodes   |很少考|
|Medium|105|  Construct Binary Tree from preorder and Inorder Traversal  |很少考|
|Medium|106|  Construct Binary Tree from Inorder and Postorder Traversal  |很少考|
|Medium|116|  Populating Next Right Pointers in Each Node |重要|
|Hard|117|  Populating Next Right Pointers in Each Node II  |重要|
|Medium|314|  Binary Tree Vertical Order Traversal    |重要|
|Medium|96    |Unique Binary Search Trees |重要|
|Medium|95    |Unique Binary Search Trees II  |很少考|
|Medium|331|  Verify preorder Serialization of a Binary Tree |很少考|
