# 0682: Baseball Game

### Description
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings <code>operations</code>, where <code>operations[i]</code> is the <code>ith</code> operation you must apply to the record and is one of the following:

An integer <code>x</code>.
Record a new score of <code>x</code>.

<code>'+'</code>.
Record a new score that is the sum of the previous two scores.

<code>'D'</code>.
Record a new score that is the double of the previous score.

<code>'C'</code>.
Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: ops = ["5","2","C","D","+"]</strong>
<strong>Output: 30</strong>
<strong>Explanation: "5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: ops = ["5","-2","4","C","D","9","+","+"]</strong>
<strong>Output: 27</strong>
<strong>Explanation: "5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: ops = ["1","C"]</strong>
<strong>Output: 0</strong>
<strong>Explanation: "1" - Add 1 to the record, record is now [1].
"C" - Invalidate and remove the previous score, record is now [].
Since the record is empty, the total sum is 0.</strong>
</pre>

### Constraints
<ul>
	<li>1 <= operations.length <= 1000</li>
	<li>operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].</li>
	<li>For operation "+", there will always be at least two previous scores on the record.</li>
    <li>For operations "C" and "D", there will always be at least one previous score on the record.</li>
</ul>

