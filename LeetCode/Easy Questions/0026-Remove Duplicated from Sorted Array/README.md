# 0026: Remove Duplicates from Sorted Array

### Description
Given an integer array <code>nums</code> sorted in <b>non-decreasing order</b>, remove the duplicates <b>in-place</b> such that each unique element appears only once. The <b>relative order</b> of the elements should be kept the same. Then return the number of <b>unique elements</b> in <code>nums</code>.

Consider the number of unique elements of <code>nums</code> to be <code>k</code>, to get accepted, you need to do the following things:
<ul>
<li>Change the array <code>nums</code> such that the first <code>k</code> elements of <code>nums</code> contain the unique elements in the order they were present in <code>nums</code> initially. The remaining elements of <code>nums</code> are not important as well as the size of <code>nums</code>.</li>
<li>Return k.</li>
</ul>
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: nums = [1,1,2]</strong>
<strong>Output: 2, nums = [1,2,_]</strong>
<strong>Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: nums = [0,0,1,1,1,2,2,3,3,4]</strong>
<strong>Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]</strong>
<strong>Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).</strong>
</pre>

### Constraints
<ul>
	<li>1 <= nums.length <= 3 * 10^4</li>
	<li>-100 <= nums[i] <= 100</li>
	<li>nums is sorted in non-decreasing order.</li>
</ul>

