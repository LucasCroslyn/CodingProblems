# 1122: Relative Sort Array

### Description
Given two arrays <code>arr1</code> and <code>arr2</code>, the elements of <code>arr2</code> are distinct, and all elements in <code>arr2</code> are also in <code>arr1</code>.

Sort the elements of arr1 such that the relative ordering of items in <code>arr1</code> are the same as in <code>arr2</code>. Elements that do not appear in <code>arr2</code> should be placed at the end of <code>arr1</code> in <b>ascending</b> order.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]</strong>
<strong>Output: [2,2,2,1,4,3,3,9,6,7,19]</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]</strong>
<strong>Output: [22,28,8,6,17,44]</strong>
</pre>

### Constraints
<ul>
	<li>1 <= arr1.length, arr2.length <= 1000</li>
	<li>0 <= arr1[i], arr2[i] <= 1000</li>
    <li>All the elements of arr2 are distinct.</li>
	<li>Each arr2[i] is in arr1.</li>
</ul>