# 0146: LRU Cache

### Description
Design a data structure that follows the constraints of a <b>Least Recently Used (LRU) cache</b>.

Implement the <code>LRUCache</code> class:

<code>LRUCache(int capacity)</code> Initialize the LRU cache with positive size <code>capacity</code>.

<code>int get(int key)</code> Return the value of the <code>key</code> if the key exists, otherwise return <code>-1</code>.

<code>void put(int key, int value)</code> Update the value of the <code>key</code> if the <code>key</code> exists. Otherwise, add the <code>key-value</code> pair to the cache. If the number of keys exceeds the <code>capacity</code> from this operation, evict the least recently used key.

The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.

### Examples

<p><strong>Example 1:</strong></p>

<pre><strong>Input: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]</strong>
<strong>Output: [null, null, null, 1, null, -1, null, -1, 3, 4]</strong>
<strong>Explanation: LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4</strong>
</pre>

### Constraints
<ul>
	<li>1 <= capacity <= 3000</li>
	<li>0 <= key <= 10^4</li>
	<li>0 <= value <= 10^5</li>
    <li>At most 2 * 105 calls will be made to get and put.</li>
</ul>

