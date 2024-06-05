# 2486: Append Characters to String to Make Subsequence

### Description

You are given two strings <code>s</code> and <code>t</code> consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of <code>s</code> so that <code>t</code> becomes a <b>subsequence</b> of <code>s</code>.

A <b>subsequence</b> is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: s = "coaching", t = "coding"</strong>
<strong>Output: 4</strong>
<strong>Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("<b>co</b>aching<b>ding</b>").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: s = "abcde", t = "a"</strong>
<strong>Output: 0</strong>
<strong>Explanation: t is already a subsequence of s ("<b>a</b>bcde").</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: s = "z", t = "abcde"</strong>
<strong>Output: 5</strong>
<strong>Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("z<b>abcde</b>").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.</strong>
</pre>

### Constraints

<ul>
	<li>1 <= s.length, t.length <= 10^5
</li>
	<li>s and t consist only of lowercase English letters.</li>
</ul>
