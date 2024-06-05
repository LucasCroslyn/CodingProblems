# 0383: Ransom Note

### Description

Given two strings <code>ransomNote</code> and <code>magazine</code>, return <b>true</b> if <code>ransomNote</code> can be constructed by using the letters from <code>magazine</code> and <b>false</b> otherwise.

Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: ransomNote = "a", magazine = "b"</strong>
<strong>Output: false</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: ransomNote = "aa", magazine = "ab"</strong>
<strong>Output: false</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: ransomNote = "aa", magazine = "aab"</strong>
<strong>Output: true</strong>
</pre>

### Constraints

<ul>
	<li>1 <= ransomNote.length, magazine.length <= 10^5</li>
	<li>ransomNote and magazine consist of lowercase English letters.</li>
</ul>
