# 1480: Running Sum of 1D Array

### Description

Given an array <code>nums</code>. We define a running sum of an array as <code>runningSum[i] = sum(nums[0]…nums[i])</code>.

Return the running sum of <code>nums</code>.

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [1,2,3,4]</strong>
<strong>Output: [1,3,6,10] </strong>
<strong>Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [1,1,1,1,1]</strong>
<strong>Output: [1,2,3,4,5]</strong>
<strong>Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: nums = [3,1,2,10,1]</strong>
<strong>Output: [3,4,6,16,17]</strong>
</pre>

<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 <= nums.length <= 1000</code></li>
<li><code>-10^6 <= nums[i] <= 10^6</code></li>
</ul>
