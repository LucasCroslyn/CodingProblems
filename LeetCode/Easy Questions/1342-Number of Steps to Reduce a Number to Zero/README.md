# 1342: Number of Steps to Reduce a Number to Zero

### Description

Given an integer <code>num</code>, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by <code>2</code>, otherwise, you have to subtract <code>1</code> from it.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: num = 14</strong>
<strong>Output: 6</strong>
<strong>Explanation: Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: num = 8</strong>
<strong>Output: 4</strong>
<strong>Explanation: Step 1) 8 is even; divide by 2 and obtain 4. 
Step 2) 4 is even; divide by 2 and obtain 2. 
Step 3) 2 is even; divide by 2 and obtain 1. 
Step 4) 1 is odd; subtract 1 and obtain 0.</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: num = 123</strong>
<strong>Output: 12</strong>
</pre>

### Constraints

<ul>
	<li>0 <= num <= 10^6</li>
</ul>
