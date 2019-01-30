> 优先队列和堆

堆是一颗具有特定性质的二叉树，堆的基本要求就是堆中所有结点的值必须大于或等于（或小于或等于）其孩子结点的值，这也称为堆的性质 [[0]](https://www.cnblogs.com/wmyskxz/p/9301021.html)


队列：先进先出
优先队列：最大优先队列，最大先出
最小优先队列，最小先出 [[1]](https://blog.csdn.net/qian520ao/article/details/80531150)

优先队列是基于堆的完全二叉树,它和队列的概念无关。(它并不是队列,而是树) [[2]](http://www.sohu.com/a/256022793_478315)

A:Priority queues are "queues" in one sense of the word, in that elements wait their turn. They are not a subtype of the Queue abstract data type.
Q:then why are they called priority Queue?
A:Because they are "queues" in the common (non-ADT) sense of the word: they are places where members arrive, wait for their turn, and then leave. The `Queue` ADT is a "queue" in which the member who has been waiting the longest is picked next. The `Priority Queue` ADT is a "queue" in which the member with highest priority is picked next. [[3]](https://stackoverflow.com/questions/19453616/are-priority-queues-really-queues)

Priority queue is an abstract data type (an interface definition) that defines three operations: *is_empty*, *insert_with_priority*, and *pull_highest_priority_element*. The definition says what those functions are expected to do, but it doesn't say how it is to be implemented.

A binary heap is one way to implement a priority queue. Its advantages are ease of implementation and that it is reasonably efficient. It's not necessarily the most efficient way to implement a priority queue (see below). Whereas a heap is definitely a priority queue, by no means is it true that a priority queue is a heap. [[4]](https://stackoverflow.com/questions/48795979/what-is-the-difference-between-a-priority-queue-and-a-min-max-heap)

也就是说：

优先队列，名字里带队列，形式上是一种队列的形式，但其实是一种独立的抽象数据类型，可以用二叉堆这种特殊的树结构实现。


![最小堆](https://github.com/Vida42/Leetcode/blob/master/Pic/min-heap.png)


[0] [数据结构与算法(4)——优先队列和堆](https://www.cnblogs.com/wmyskxz/p/9301021.html)

[1] [算法 —— 排序 —— 优先队列](https://blog.csdn.net/qian520ao/article/details/80531150)

[2] [漫画：什么是优先队列？](http://www.sohu.com/a/256022793_478315)

[3] [Are Priority Queues really Queues?](https://stackoverflow.com/questions/19453616/are-priority-queues-really-queues)

[4] [What is the difference between a priority queue and a min / max heap?](https://stackoverflow.com/questions/48795979/what-is-the-difference-between-a-priority-queue-and-a-min-max-heap)

[5] [堆——神奇的优先队列(上) 【经典】](https://www.cnblogs.com/chenweichu/articles/5710567.html)


## PriorityQueue：0 / 7

|     |     |     |    |  PriorityQueue  |
| --- | --- | --- | --- | --- |
||215|	Kth Largest Element in an Array	|||
||347|	Top K Frequent Elements	|||
||313|	Super Ugly Number	|很少考||
||373|	Find K Pairs with Smallest Sums	|很少考||
||218|	The Skyline Problem	|||
||332|	Reconstruct Itinerary	|||
||341|	Flatten Nested List Iterator|||

