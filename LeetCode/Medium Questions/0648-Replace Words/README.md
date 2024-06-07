# 0648: Replace Words

### Description
In English, we have a concept called <b>root</b>, which can be followed by some other word to form another longer word - let's call this word <b>derivative</b>. For example, when the <b>root</b> "help" is followed by the word "ful", we can form a <b>derivative</b> "helpful".

Given a <code>dictionary</code> consisting of many <b>roots</b> and a <code>sentence</code> consisting of words separated by spaces, replace all the <b>derivatives</b> in the <code>sentence</code> with the <b>root</b> forming it. If a <b>derivative</b> can be replaced by more than one <b>root</b>, replace it with the <b>root</b> that has the shortest length.

Return the <code>sentence</code> after the replacement.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"</strong>
<strong>Output: "the cat was rat by the bat"</strong>
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"</strong>
<strong>Output: "a a b c"</strong>
</pre>

### Constraints
<ul>
	<li>1 <= dictionary.length <= 1000</li>
	<li>1 <= dictionary[i].length <= 100</li>
	<li>dictionary[i] consists of only lower-case letters.</li>
    <li>1 <= sentence.length <= 10^6</li>
    <li>sentence consists of only lower-case letters and spaces.</li>
    <li>The number of words in sentence is in the range [1, 1000]</li>
    <li>The length of each word in sentence is in the range [1, 1000]</li>
    <li>Every two consecutive words in sentence will be separated by exactly one space.</li>
    <li>sentence does not have leading or trailing spaces.</li>
</ul>

