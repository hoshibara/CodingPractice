这道题的描述有问题
直接看英文描述吧
> You are given an integer array nums and a non-negative integer k. 
> 
> A sequence of integers seq is called good if there are at most `k` indices `i` in the range `[0, seq.length - 2]` such that `seq[i] != seq[i + 1]`. 
> 
> Return the maximum possible length of a good subsequence of nums.

意思其实就是i的取值范围是`[0, seq.length - 2]`，这个范围其实也就是在子序列内比较完除最后一位的数字（最后一位越界了）。

子序则是：

> A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

即可以删除一些元素

实例也有问题

```text
Example 1:

Input: nums = [1,2,1,1,3], k = 2

Output: 4

Explanation:

The maximum length subsequence is [1,2,1,1,3].

应为: [1, 2, 1, 1] [1, 1, 1, 3] [2, 1, 1, 3] 

Example 2:

Input: nums = [1,2,3,4,5,1], k = 0

Output: 2

Explanation:

The maximum length subsequence is [1,2,3,4,5,1].

应为: [1, 1] 
```
看上去是个k为y轴的二维动规

