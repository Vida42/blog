# Note About Data Structure and Algorithm <!-- omit in toc -->

![](https://img.shields.io/badge/CurrentStatus-HardWorking-red)

---

Table of contents

- [Data Structure](#data-structure)

    - [ArrayList](#array-list)

    - [LinkedList](#linked-list)

    - [HashMap](#hashmap)

    - [HashSet](#hashset)

    - [Queue](#queue)

    - [Stack](#stack)

    - [Tree](#tree)

    - [Heap](#heap)

- [Sort](#sort)


- [Algorithm](#algorithm)

    - [Recursion](#recursion)

    - [Divide and Conquer](#divide-and-conquer)

    - [Dynamic Programming](#dynamic-programming)

    - [Greedy Algorithm](#greedy-algorithm)

    - [Backtracking](#backtracking)

    - [Branch and Bound](#branch-and-bound)


---


# Data Structure

## ArrayList

## LinkedList

## HashMap

## HashSet

## Queue

## Stack

## Tree

## Heap


# Sort

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

## Quck Sort

## Merge Sort

## Selection Sort

## Heap Sort

## Insertion Sort

## Shell Sort

## Bubble Sort

## Bucket Sort

## Counting Sort

## Radix Sort


# Algorithm

## Recursion

## Divide and Conquer

## Dynamic Programming

## Greedy Algorithm

## Backtracking

## Branch and Bound