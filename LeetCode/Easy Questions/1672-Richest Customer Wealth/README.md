# 1672: Richest Customer Wealth

### Description

You are given an<code> m x n</code> integer grid <code>accounts</code> where <code>accounts[i][j]</code> is the amount of money the <code>i​​​​​​​​​​​th​​​​</code> customer has in the <code>j​​​​​​​​​​​th​​​​</code> bank. Return the <b>wealth</b> that the richest customer has.

A customer's <b>wealth</b> is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum <b>wealth</b>.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: accounts = [[1,2,3],[3,2,1]]</strong>
<strong>Output: 6</strong>
<strong>Explanation: <code>1st customer has wealth = 1 + 2 + 3 = 6</code>
<code>2nd customer has wealth = 3 + 2 + 1 = 6</code>
Both customers are considered the richest with a wealth of 6 each, so return 6.</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: accounts = [[1,5],[7,3],[3,5]]</strong>
<strong>Output: 10</strong>
<strong>Explanation: <code>1st customer has wealth = 6</code>
<code>2nd customer has wealth = 10 </code>
<code>3rd customer has wealth = 8</code>
The 2nd customer is the richest with a wealth of 10.</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]</strong>
<strong>Output: 17</strong>
</pre>

### Constraints

<ul>
	<li>m == accounts.length</li>
	<li>n == accounts[i].length</li>
	<li>1 <= m, n <= 50</li>
    <li>1 <= accounts[i][j] <= 100</li>
</ul>
