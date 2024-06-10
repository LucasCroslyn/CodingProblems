# 1929: Concatenation of Array

### Description
Given an integer array <code>nums</code> of length <code>n</code>, you want to create an array <code>ans</code> of length <code>2n</code> where <code>ans[i] == nums[i]</code> and <code>ans[i + n] == nums[i]</code> for <code>0 <= i < n</code> (0-indexed).

Specifically, <code>ans</code> is the concatenation of two <code>nums</code> arrays.

Return the array <code>ans</code>.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [1,2,1]</strong>
<strong>Output: [1,2,1,1,2,1]</strong>
<strong>Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [1,3,2,1]</strong>
<strong>Output: [1,3,2,1,1,3,2,1]</strong>
<strong>Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]</strong>
</pre>

### Constraints
<ul>
	<li>n == nums.length</li>
	<li>1 <= n <= 1000</li>
	<li>1 <= nums[i] <= 1000</li>
</ul>

