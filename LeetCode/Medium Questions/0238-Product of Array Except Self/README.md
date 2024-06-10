# 0238: Product of Array Except Self

### Description
Given an integer array <code>nums</code>, return an array answer such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.

The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a <b>32-bit integer</b>.

You must write an algorithm that runs in <code>O(n)</code> time and without using the division operation.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [1,2,3,4]</strong>
<strong>Output: [24,12,8,6]</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [-1,1,0,-3,3]</strong>
<strong>Output: [0,0,9,0,0]</strong>
</pre>

### Constraints
<ul>
	<li>2 <= nums.length <= 10^5</li>
	<li>-30 <= nums[i] <= 30</li>
	<li>The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.</li>
</ul>

