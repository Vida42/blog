# OUTLINE
## Linked List
- Dummy Node
    - 25. Reverse Nodes in k-Groups
    - 86. Partition List
    - 21. Merge Two Sorted Lists
    - 92. Reverse Linked List II
    - 143. Reorder List
    - 61. Rotate List
    - [511. Swap Two Nodes in Linked List](https://www.lintcode.com/problem/swap-two-nodes-in-linked-list/description)(Lintcode)

- High Frequency
    - 138. Copy List with Random Pointer
    - 141. Linked List Cycle
    - 142. Linked List Cycle II
    - 160. Intersection of Two Linked Lists

    - 148. Sort List
    - 237. Delete Node in a Linked List
    - 109. Convert Sorted List to Binary Search Tree
    - 426. Convert Binary Search Tree to Sorted Doubly Linked List[LOCK]

## Array
- Subarray
    - 53. Maximum Subarray
    - 643. Maximum Average Subarray I
    - 560. Subarray Sum Equals K
    - [139. Subarray Sum Closest](https://www.lintcode.com/problem/subarray-sum-closest/description)(Lintcode)

- Sorted Array
    - 88. Merge Sorted Array
    - 349. Intersection of Two Arrays
    - 4. Median of Two Sorted Arrays


# Linked List

链表有寻址操作，比数组慢。即使复杂度一样。

> 以下代码两个print一样的解释

node占4字节，node.val占4字节，node.next占4字节

node2赋给node1，node1变了，.val和.next也变了。

但是head没变，还是指向原node1的val和next

改node没有改链表的结构，只是改了reference

内存里链表的结构没变。

```java
void print(){
    while (node != null) {
    ...println(node.val);
    node = node.next;
    }
}

ListNode node1 = new ListNode(1);
ListNode node2 = new ListNode(2);
ListNode node3 = new ListNode(3);

node1.next = node2;
node2.next = node3;

ListNode head = node1;

print(head);
// 1->2->3

node1 = node2;
prtin(head);
// 1->2->3
```

### 25. Reverse Nodes in k-Groups

大部分链表的题，谈不上什么算法，考验基本功底。考验你怎么操作指针。

## Dummy Node
> [八问八答](https://www.jiuzhang.com/qa/4599/)

链表大部分都是结构在变，这时使用dummy

举例，搞1，2，3，三个点去做，画图解决，这种能解决大部分


如何使用 Dummy Node
> dummy; head = dummy

新笔记：

**链表的结构大部分可以这么写**：

```
dummy = ListNode(0)
dummy.next = head

return dummy.next
```

> dummy node一般指向链表的头结点head，使得链表的每一个节点都有一个前驱，方便操作，即使链表的头部发生变化，我们不需要修改head，只需要找到dummy.next 即可

head = dummy 这句话总是需要么？
> 表示当前从哨兵节点开始往后遍历，dummy作为新的起始点。

为了减少混淆，他用了prev=dummy,这句话可以删掉，是个历史遗留问题

什么时候使用 Dummy Node?
> 如果你的链表操作可能涉及到修改head的时候，需要使用dummy node，来简化程序复杂度，但不是必须的。

当链表结构发生变化时，就需要dummy node

Dummy Node 是否需要删除？
> no

使用 Dummy Node 算面试官会说我耗费了额外空间么？
> no, O(1)额外

Dummy Node 非用不可么？
> 不是必须的，但是能大大简化你程序的逻辑。

Dummy Node 初始化的值重要么？
> 一点都不重要，一般情况我们初始化为0，-1，1

链表的问题都需要用到 Dummy Node 么？
> 绝大多数都可以用，可以简化程序逻辑。

## 用到了 Dummy Node 的值得一做的题目

### 86. Partition List

双指针的Dummy啊！因为知识指来指去，所以空间复杂度O(1).

### 21. Merge Two Sorted Lists

Still 双指针的Dummy

### 92. Reverse Linked List II

又懵了。切进要revese的范围内reverse，最后再连起来。

### 143. Reorder List

### 61. Rotate List

形成闭环，然后找新的tail

### [511. Swap Two Nodes in Linked List](https://www.lintcode.com/problem/swap-two-nodes-in-linked-list/description)(Lintcode)


## High Frequency

<font color=#cc0099>高频中的高频</font>

### (138. Copy List with Random Pointer](https://www.jiuzhang.com/solutions/copy-list-with-random-pointer/)

用map可以实现O(n)空间

关键在于如何实现O(1)空间

着眼点不在于想不想得到，在于知道算法怎么写出来，可以拿来练习链表操作。

### 141. Linked List Cycle

- 空间O(n):
> 用列表判断：如果.next已在列表内，有环

- 空间O(1):
> 快慢指针

follow up:

142. Linked List Cycle II

- 空间O(n):
> 同上，返回该重合点即可

- 空间O(1):
> 快慢指针

160. Intersection of Two Linked Lists

两个指针各自走各自的，然后交换再走一遍。

### (148. Sort List)[https://www.jiuzhang.com/solutions/sort-list/]

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

问：哪些排序算法时间复杂度是 O(nlogn) 的？

merge sort, quick sort, heap sort

问：哪些排序算法空间复杂度是 O(1) 的？

quick sort

但在链表里，Merge的空间也可以是O(1)因为只对指针操作


### 237. Delete Node in a Linked List

四行解决

### 109. Convert Sorted List to Binary Search Tree

每次找到中点，然后递归去对两边做一样的事。

### 426. Convert Binary Search Tree to Sorted Doubly Linked List[LOCK]

中序遍历递归

# Array

## Subarray

### 53. Maximum Subarray

### 643. Maximum Average Subarray I

和[604. Window Sum](https://www.lintcode.com/problem/window-sum/description)(Lintcode)一样👉[Soultion](https://www.jiuzhang.com/solutions/window-sum/#tag-lang-python)

### 560. Subarray Sum Equals K

和Lintcode 138 Subarray Sum 一样

### [139. Subarray Sum Closest](https://www.lintcode.com/problem/subarray-sum-closest/description)(Lintcode)


## Sorted Array

### 88. Merge Sorted Array

https://www.jiuzhang.com/solutions/merge-sorted-array/
https://www.jiuzhang.com/solutions/merge-two-sorted-arrays/

### 349. Intersection of Two Arrays

### [数组内积](https://www.jiuzhang.com/qa/1832/)

### 4. Median of Two Sorted Arrays
