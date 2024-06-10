# 0027: Remove Element

### Description
Given an integer array <code>nums</code> and an integer <code>val</code>, remove all occurrences of <code>val</code> in <code>nums</code> in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in <code>nums</code> which are not equal to <code>val</code> be <code>k</code>, to get accepted, you need to do the following things:

Change the array <code>nums</code> such that the first k elements of <code>nums</code> contain the elements which are not equal to <code>val</code>. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.
Return <code>k</code>.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [3,2,2,3], val = 3</strong>
<strong>Output: 2, nums = [2,2,_,_]</strong>
<strong>Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [0,1,2,2,3,0,4,2], val = 2</strong>
<strong>Output: 5, nums = [0,1,4,0,3,_,_,_]</strong>
<strong>Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).</strong>
</pre>

### Constraints
<ul>
	<li>0 <= nums.length <= 100</li>
	<li>0 <= nums[i] <= 50</li>
	<li>0 <= val <= 100</li>
</ul>

