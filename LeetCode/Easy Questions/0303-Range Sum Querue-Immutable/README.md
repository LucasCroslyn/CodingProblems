# 0303: Range Sum Query - Immutable

### Description
Given an integer array <code>nums</code>, handle multiple queries of the following type:

Calculate the <b>sum</b> of the elements of <code>nums</code> between indices left and right inclusive where <code>left <= right</code>.

Implement the <code>NumArray</code> class:

<code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.

<code>int sumRange(int left, int right)</code> Returns the sum of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: ["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]</strong>
<strong>Output: [null, 1, -1, -3]</strong>
<strong>Explanation: NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3</strong>
</pre>

### Constraints
<ul>
	<li>1 <= nums.length <= 10^4</li>
	<li>-10^5 <= nums[i] <= 10^5</li>
	<li>0 <= left <= right < nums.length</li>
    <li>At most 104 calls will be made to sumRange.</li>
</ul>

