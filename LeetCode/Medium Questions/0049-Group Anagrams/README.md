# 0049: Group Anagrams

### Description
Given an array of strings <code>strs</code>, group the <b>anagrams</b> together. You can return the answer in <b>any order</b>.

An <b>Anagram</b> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: strs = ["eat","tea","tan","ate","nat","bat"]</strong>
<strong>Output: [["bat"],["nat","tan"],["ate","eat","tea"]]</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: strs = [""]</strong>
<strong>Output: [[""]]</strong>
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input: strs = ["a"]</strong>
<strong>Output: [["a"]]</strong>
</pre>

### Constraints
<ul>
	<li>1 <= strs.length <= 10^4</li>
	<li>0 <= strs[i].length <= 100</li>
	<li>strs[i] consists of lowercase English letters.</li>
</ul>