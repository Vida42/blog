# Outline

## 双指针

- 同向双指针
    - 643. Maximum Average Subarray I
    - 283. Move Zeroes
    - 26. Remove Duplicates from Sorted Array
    - 80. Remove Duplicates from Sorted Array II

- 相向双指针
    - 125. Valid Palindrome
    - 796. Rotate String
    - 167. Two Sum II - Input array is sorted

## Two Sum(考的多)

- 1. Two Sum
- [L]170. Two Sum III - Data structure design
- 15. 3Sum
- 611. Valid Triangle Number
- 16. 3Sum Closest
- 18. 4Sum
- [L]1099. Two Sum Less Than K

## Partition(考的多)

- Quick Select
    - 215. Kth Largest Element in an Array

- 分成两个部分
    - L 31. Partition Array
    - 905. Sort Array By Parity
    - L 144. Interleaving Positive And Negative Numbers

- 分成三个部分
    - 75. Sort Colors
    - L143. Sort Colors II(分成k个部分)


# 双指针

两根指针入门题（时间复杂度都是n）

## 同向双指针
### 283. Move Zeroes
### 26. Remove Duplicates from Sorted Array
### 80. Remove Duplicates from Sorted Array II

## 相向双指针
### 125. Valid Palindrome

```python
isalnum()
# returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False.

isalpha()

isdigit()
```

0-9数字的ASCII十进制编码为48-57

大写字母的ASCII十进制编码为65-90

小写字母的ASCII十进制编码为97-122

### 796. Rotate String

Is String slicing's time complexity O(1)?

### 167. Two Sum II - Input array is sorted

# Two Sum

### 1. Two Sum

Hashmap

> Two Sum Unique Pair:

[1,1,2,4,5,6,6], target: 7

这时不能返回重复，sort后two pointers

也可以继续用hashmap/set方法：

```python
def uniqueTwoSum(nums, target):
    dic = set()
    seen = set()
    count = 0
    for i in nums:
        sub = target - i
        # 因为sub和i如果是一个解，已全部放入seen，所以用一个判断即可
        if sub in dic and sub in seen:
            count += 1
            seen.add(i)
            seen.add(sub)
        else:
            dic.add(i)
    return count
```

### 170. Two Sum III - Data structure design

two sum套一个类

### 15. 3Sum

将一个数作为target，再用Two Sum Unique Pair的思想

### 611. Valid Triangle Number

类two sum题目，只是判断条件改变了

### 16. 3Sum Closest

**看一下笔记里的！！**

### 18. 4Sum

套3Sum

### 1099. Two Sum Less Than K

less than or equal to target

greater than or equal to target

都得会

> two sum closest to target

[-1, 2, 1, -4], 4

结果：4-(2+1)=1，最小

还是双指针挪动。
如果和比现在大，l右移只会使和更大，这样差值也更大，所以r左移；
如果和比现在小，r左移只会使和更小，这样差值也更大，所以l右移；


```python
def twoSumClosest(nums, target):
    nums.sort()
    i, j = 0, len(nums)-1
    res = float('inf')
    while i < j:
        print(nums[i], nums[j])
        res = min(res, abs(nums[i] + nums[j] - target))
        if nums[i] + nums[j] < target:
            i += 1
        else:
            j -= 1
    return res
```


# Partition

## 分成两个部分

### 905. Sort Array By Parity

two pointers,顺序不符合输出时，互换。

### L 31. Partition Array

用了`905. Sort Array By Parity`中的解法。

注意一开始判断边界
```python
        if not nums or len(nums) == 0:
            return 0
```

第二种写法是先把两指针挪到第一个应该互换的位置，然后互换。

### L 144. Interleaving Positive And Negative Numbers

先分成正负两子块，再互换。

## 分成三个部分

### 75. Sort Colors

follow up：

### L143. Sort Colors II

每次以O(n)的复杂度把列表对半分。

## Quick Select

完全排序可以在O(nlogn)复杂度完成，不完全排序可以在O(N)复杂度完成。

### 215. Kth Largest Element in an Array


# 总结

## Two Sum
- = target
- <= target
- > target
- unique pairs
- closest to target
- difference = target

## Partition
- Quick Select
- 分成两个部分
- 分成三个部分