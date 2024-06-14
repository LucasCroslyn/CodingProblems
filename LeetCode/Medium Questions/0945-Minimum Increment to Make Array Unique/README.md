# 0945: Minimum Increment to Make Array Unique

### Description

You are given an integer array <code>nums</code>. In one move, you can pick an index <code>i</code> where <code>0 <= i < nums.length</code> and increment <code>nums[i]<code> by <code>1</code>.

Return the <code>minimum number</code> of moves to make every value in <code>nums</code> unique.

The test cases are generated so that the answer fits in a 32-bit integer.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [1,2,2]</strong>
<strong>Output: 1</strong>
<strong>Explanation: After 1 move, the array could be [1, 2, 3].</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [3,2,1,2,1,7]</strong>
<strong>Output: 6</strong>
<strong>Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.</strong>
</pre>

### Constraints

<ul>
	<li>1 <= nums.length <= 10^5</li>
	<li>0 <= nums[i] <= 10^5</li>
</ul>
