<h2><a href="https://leetcode.com/problems/count-occurrences-in-text/">2738. Count Occurrences in Text</a></h2><h3>Medium</h3><hr><div class="sql-schema-wrapper__3VBi" bis_skin_checked="1"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div bis_skin_checked="1"><p>Table:<font face="monospace"> <code>Files</code></font></p>

<pre>+-------------+---------+
| Column Name | Type    |
+-- ----------+---------+
| file_name   | varchar |
| content     | text    |
+-------------+---------+
file_name is the column with unique values of this table. 
Each row contains file_name and the content of that file.
</pre>

<p>Write a solution to find&nbsp;the number of files that have at least one occurrence of the words&nbsp;<strong>'bull'</strong> and <strong>'bear'</strong> as a <strong>standalone word</strong>, respectively, disregarding any instances where it appears without space on either side (e.g. 'bullet',&nbsp;'bears', 'bull.',&nbsp;or 'bear'&nbsp;at the beginning or end of a sentence will <strong>not</strong> be considered)&nbsp;</p>

<p>Return <em>the word 'bull' and 'bear' along with the corresponding number of occurrences in <strong>any order.</strong></em></p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong>&nbsp;
Files table:
+------------+----------------------------------------------------------------------------------+
| file_name  | contenet                                                                         | 
+------------+----------------------------------------------------------------------------------+
| draft1.txt | The stock exchange predicts a bull market which would make many investors happy. | 
| draft2.txt | The stock exchange predicts a bull market which would make many investors happy, |
|&nbsp;           | but analysts warn of possibility of too much optimism and that in fact we are    |
|&nbsp;           | awaiting a bear market.                                                          | 
| draft3.txt | The stock exchange predicts a bull market which would make many investors happy, |
|&nbsp;           | but analysts warn of possibility of too much optimism and that in fact we are    |
|&nbsp;           | awaiting a bear market. As always predicting the future market is an uncertain   |
|            | game and all investors should follow their instincts and best practices.         | 
+------------+----------------------------------------------------------------------------------+
<strong>Output:</strong>&nbsp;
+------+-------+
| word | count | &nbsp;
+------+-------+
| bull |&nbsp;3     |&nbsp;
| bear |&nbsp;2     | 
+------+-------+
<strong>Explanation:</strong>&nbsp;
- The word "bull" appears 1 time in "draft1.txt", 1 time in "draft2.txt", and 1 time in "draft3.txt". Therefore, the total number of occurrences for the word "bull" is 3.
- The word "bear" appears 1 time in "draft2.txt", and 1 time in "draft3.txt". Therefore, the total number of occurrences for the word "bear" is 2.

</pre>
</div>