# 0304: Range Sum Query 2D - Immutable

### Description
Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type:

Calculate the <b>sum</b> of the elements of <code>matrix</code> inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the <code>NumMatrix</code> class:

<code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code>matrix</code>.

<code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the <b>sum</b> of the elements of <code>matrix</code> inside the rectangle defined by its <b>upper left corner</b> <code>(row1, col1)</code> and <b>lower right corner</b> <code>(row2, col2)</code>.

You must design an algorithm where <code>sumRegion</code> works on <code>O(1)</code> time complexity.

### Examples

<p><strong>Example 1:</strong></p>

![Sum Grid](sum-grid.jpg "Sum Grid")

<pre><strong>Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]</strong>
<strong>Output: [null, 8, 11, 12]</strong>
<strong>Explanation: NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)</strong>
</pre>

### Constraints
<ul>
	<li>m == matrix.length</li>
	<li>n == matrix[i].length</li>
	<li>1 <= m, n <= 200</li>
    <li>-10^4 <= matrix[i][j] <= 10^4</li>
    <li>0 <= row1 <= row2 < m</li>
    <li>0 <= col1 <= col2 < n</li>
    <li>At most 104 calls will be made to sumRegion.</li>
</ul>

