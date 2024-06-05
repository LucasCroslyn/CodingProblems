# 0001: Two Sum

### Description

Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to <code>target</code>.

You may assume that each input would have <b>exactly one solution</b>, and you may not use the same element twice.

You can return the answer in any order.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [2,7,11,15], target = 9</strong>
<strong>Output: [0, 1]</strong>
<strong>Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [3,2,4], target = 6</strong>
<strong>Output: [1,2]</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: nums = [3,3], target = 6</strong>
<strong>Output: [0,1]</strong>
</pre>

### Constraints

<ul>
	<li>2 <= nums.length <= 10^4</li>
	<li>-10^9 <= nums[i] <= 10^9</li>
	<li>-10^9 <= target <= 10^9</li>
    <li>Only one valid answer exists.</li>
</ul>
