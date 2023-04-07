# https://leetcode.com/problems/triangle/description/

from functools import lru_cache
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dfs(depth: int, i: int):
            if depth == len(triangle):
                return 0

            leftButtom = dfs(depth + 1, i)
            rightButtom = dfs(depth + 1, i + 1)

            return min(triangle[depth][i] + leftButtom, triangle[depth][i] + rightButtom)

        return dfs(0, 0)




	392
Is Subsequence	47.6%	Easy
894
All Possible Full Binary Trees	80.0%	Medium
1641
Count Sorted Vowel Strings	77.4%	Medium
1277
Count Square Submatrices with All Ones	74.5%	Medium
2436
Minimum Split Into Subarrays With GCD Greater Than One
73.9%	Medium
2393
Count Strictly Increasing Subarrays
72.9%	Medium
22
Generate Parentheses	72.5%	Medium
1043
Partition Array for Maximum Sum	71.6%	Medium
1706
Where Will the Ball Fall	71.5%	Medium
1638
Count Substrings That Differ by One Character	71.4%	Medium
1884
Egg Drop With 2 Eggs and N Floors	70.9%	Medium
1387
Sort Integers by The Power Value	70.1%	Medium
877
Stone Game	69.7%	Medium
931
Minimum Falling Path Sum	69.1%	Medium
1525
Number of Good Ways to Split a String	68.9%	Medium
1130
Minimum Cost Tree From Leaf Values	68.3%	Medium
750
Number Of Corner Rectangles
67.5%	Medium
2431
Maximize Total Tastiness of Purchased Fruits
67.3%	Medium
1395
Count Number of Teams	67.2%	Medium
647
Palindromic Substrings	66.9%	Medium
2533
Number of Good Binary Strings
66.0%	Medium
983
Minimum Cost For Tickets	65.9%	Medium
2304
Minimum Path Cost in a Grid	65.9%	Medium
1227
Airplane Seat Assignment Probability	65.6%	Medium
2495
Number of Subarrays Having Even Product
65.3%	Medium
714
Best Time to Buy and Sell Stock with Transaction Fee	65.2%	Medium
413
Arithmetic Slices	65.1%	Medium
131
Palindrome Partitioning	64.9%	Medium
1140
Stone Game II	64.7%	Medium
1908
Game of Nim
64.5%	Medium
526
Beautiful Arrangement	64.4%	Medium
122
Best Time to Buy and Sell Stock II	63.9%	Medium
241
Different Ways to Add Parentheses	63.9%	Medium
1578
Minimum Time to Make Rope Colorful	63.4%	Medium
1664
Ways to Make a Fair Array	63.3%	Medium
2189
Number of Ways to Build House of Cards
62.9%	Medium
62
Unique Paths	62.7%	Medium
712
Minimum ASCII Delete Sum for Two Strings	62.5%	Medium
1746
Maximum Subarray Sum After One Operation
62.3%	Medium
64
Minimum Path Sum	62.0%	Medium
2305
Fair Distribution of Cookies	61.8%	Medium
926
Flip String to Monotone Increasing	61.5%	Medium
256
Paint House
61.1%	Medium
516
Longest Palindromic Subsequence	61.1%	Medium
1947
Maximum Compatibility Score Sum	61.1%	Medium
518
Coin Change II	60.6%	Medium
1493
Longest Subarray of 1's After Deleting One Element	60.4%	Medium
2378
Choose Edges to Maximize Score in a Tree
60.4%	Medium
1372
Longest ZigZag Path in a Binary Tree	60.2%	Medium
553
Optimal Division	59.9%	Medium
583
Delete Operation for Two Strings	59.8%	Medium
96
Unique Binary Search Trees	59.7%	Medium
1031
Maximum Sum of Two Non-Overlapping Subarrays	59.6%	Medium
1014
Best Sightseeing Pair	59.4%	Medium
1105
Filling Bookcase Shelves	59.4%	Medium
1048
Longest String Chain	59.3%	Medium
1062
Longest Repeating Substring
59.2%	Medium
1035
Uncrossed Lines	59.2%	Medium
1911
Maximum Alternating Subsequence Sum	59.2%	Medium
1653
Minimum Deletions to Make String Balanced	58.9%	Medium
1749
Maximum Absolute Sum of Any Subarray	58.5%	Medium
1143
Longest Common Subsequence	58.4%	Medium
1690
Stone Game VII	58.1%	Medium
2110
Number of Smooth Descent Periods of a Stock	58.0%	Medium
1504
Count Submatrices With All Ones	57.5%	Medium
740
Delete and Earn	57.1%	Medium
838
Push Dominoes	57.0%	Medium
788
Rotated Digits	56.7%	Medium
646
Maximum Length of Pair Chain	56.5%	Medium
309
Best Time to Buy and Sell Stock with Cooldown	56.2%	Medium
343
Integer Break	56.1%	Medium
651
4 Keys Keyboard
55.7%	Medium
2297
Jump Game VIII
55.7%	Medium
2464
Minimum Subarrays in a Valid Split
55.7%	Medium
1039
Minimum Score Triangulation of Polygon	55.5%	Medium
1182
Shortest Distance to Target Color
55.4%	Medium
1066
Campus Bikes II
54.9%	Medium
2063
Vowels of All Substrings	54.7%	Medium
1334
Find the City With the Smallest Number of Neighbors at a Threshold Distance	54.6%	Medium
2606
Find the Substring With Maximum Cost	54.6%	Medium
120
Triangle	54.5%	Medium
2002
Maximum Product of the Length of Two Palindromic Subsequences	54.2%	Medium
1230
Toss Strange Coins
54.1%	Medium
337
House Robber III	53.9%	Medium
1155
Number of Dice Rolls With Target Sum	53.9%	Medium
650
2 Keys Keyboard	53.5%	Medium
638
Shopping Offers	53.3%	Medium
1049
Last Stone Weight II	53.2%	Medium
2510
Check if There is a Path With Equal Number of 0's And 1's
53.0%	Medium
813
Largest Sum of Averages	52.9%	Medium
790
Domino and Tromino Tiling	52.8%	Medium
279
Perfect Squares	52.7%	Medium
95
Unique Binary Search Trees II	52.4%	Medium
300
Longest Increasing Subsequence	52.2%	Medium
377
Combination Sum IV	52.2%	Medium
688
Knight Probability in Chessboard	52.1%	Medium
294
Flip Game II
51.9%	Medium
357
Count Numbers with Unique Digits	51.9%	Medium
1162
As Far from Land as Possible	51.9%	Medium
1218
Longest Arithmetic Subsequence of Given Difference	51.9%	Medium
351
Android Unlock Patterns
51.5%	Medium
361
Bomb Enemy
51.3%	Medium
718
Maximum Length of Repeated Subarray	51.3%	Medium
799
Champagne Tower	51.3%	Medium
2222
Number of Ways to Select Buildings	51.3%	Medium
486
Predict the Winner	51.1%	Medium
1626
Best Team With No Conflicts	51.1%	Medium
1262
Greatest Sum Divisible by Three	50.8%	Medium
935
Knight Dialer	50.5%	Medium
2052
Minimum Cost to Separate Sentence Into Rows
50.5%	Medium
1024
Video Stitching	50.4%	Medium
435
Non-overlapping Intervals	50.3%	Medium
53
Maximum Subarray	50.2%	Medium
562
Longest Line of Consecutive One in Matrix
50.2%	Medium
1139
Largest 1-Bordered Square	50.2%	Medium
2184
Number of Ways to Build Sturdy Brick Wall
50.1%	Medium
2571
Minimum Operations to Reduce an Integer to 0	49.9%	Medium
823
Binary Trees With Factors	49.7%	Medium
1682
Longest Palindromic Subsequence II
49.7%	Medium
487
Max Consecutive Ones II
49.6%	Medium
198
House Robber	49.4%	Medium
1824
Minimum Sideway Jumps	49.3%	Medium
2100
Find Good Days to Rob the Bank	49.1%	Medium
2380
Time Needed to Rearrange a Binary String	49.0%	Medium
376
Wiggle Subsequence	48.3%	Medium
764
Largest Plus Sign	48.3%	Medium
873
Length of Longest Fibonacci Subsequence	48.3%	Medium
2439
Minimize Maximum of Array	47.6%	Medium
1774
Closest Dessert Cost	47.3%	Medium
978
Longest Turbulent Subarray	47.2%	Medium
2266
Count Number of Texts	47.0%	Medium
375
Guess Number Higher or Lower II	46.9%	Medium
474
Ones and Zeroes	46.8%	Medium
2152
Minimum Number of Lines to Cover Points
46.8%	Medium
1027
Longest Arithmetic Subsequence	46.7%	Medium
2522
Partition String Into Substrings With Values at Most K	46.7%	Medium
2140
Solving Questions With Brainpower	46.4%	Medium
416
Partition Equal Subset Sum	46.3%	Medium
264
Ugly Number II	46.2%	Medium
1696
Jump Game VI	46.1%	Medium
494
Target Sum	45.7%	Medium
139
Word Break	45.6%	Medium
313
Super Ugly Number	45.5%	Medium
2054
Two Best Non-Overlapping Events	45.2%	Medium
221
Maximal Square	45.0%	Medium
2291
Maximum Profit From Trading Stocks
44.9%	Medium
542
01 Matrix	44.8%	Medium
2086
Minimum Number of Food Buckets to Feed the Hamsters	44.8%	Medium
2327
Number of People Aware of a Secret	44.8%	Medium
276
Paint Fence
44.5%	Medium
576
Out of Boundary Paths	44.3%	Medium
1567
Maximum Length of Subarray With Positive Product	44.1%	Medium
2008
Maximum Earnings From Taxi	43.6%	Medium
808
Soup Servings	43.5%	Medium
1524
Number of Sub-arrays With Odd Sum	43.3%	Medium
673
Number of Longest Increasing Subsequence	42.9%	Medium
918
Maximum Sum Circular Subarray	42.9%	Medium
333
Largest BST Subtree
42.8%	Medium
1621
Number of Sets of K Non-Overlapping Line Segments	42.4%	Medium
1959
Minimum Total Space Wasted With K Resizing Operations	42.3%	Medium
322
Coin Change	42.1%	Medium
2466
Count Ways To Build Good Strings	42.1%	Medium
634
Find the Derangement of An Array
42.0%	Medium
368
Largest Divisible Subset	41.5%	Medium
1186
Maximum Subarray Sum with One Deletion	41.5%	Medium
396
Rotate Function	41.2%	Medium
2036
Maximum Alternating Subarray Sum
41.1%	Medium
213
House Robber II	41.0%	Medium
2320
Count Number of Ways to Place Houses	40.6%	Medium
473
Matchsticks to Square	40.2%	Medium
845
Longest Mountain in Array	40.2%	Medium
2369
Check if There is a Valid Partition For The Array	40.2%	Medium
698
Partition to K Equal Sum Subsets	40.0%	Medium
45
Jump Game II	39.8%	Medium
2501
Longest Square Streak in an Array	39.5%	Medium
63
Unique Paths II	39.4%	Medium
1786
Number of Restricted Paths From First to Last Node	39.2%	Medium
55
Jump Game	38.9%	Medium
1888
Minimum Number of Flips to Make the Binary String Alternating	38.9%	Medium
467
Unique Substrings in Wraparound String	38.6%	Medium
2370
Longest Ideal Subsequence	37.7%	Medium
2420
Find All Good Indices	37.5%	Medium
97
Interleaving String	37.3%	Medium
898
Bitwise ORs of Subarrays	37.2%	Medium
787
Cheapest Flights Within K Stops	37.0%	Medium
2311
Longest Binary Subsequence Less Than or Equal to K	37.0%	Medium
1997
First Day Where You Have Been in All the Rooms	36.9%	Medium
1477
Find Two Non-overlapping Sub-arrays Each With Target Sum	36.7%	Medium
837
New 21 Game	36.2%	Medium
1937
Maximum Number of Points with Cost	36.0%	Medium
907
Sum of Subarray Minimums	35.8%	Medium
418
Sentence Screen Fitting
35.6%	Medium
397
Integer Replacement	35.2%	Medium
152
Maximum Product Subarray	34.9%	Medium
678
Valid Parenthesis String	34.1%	Medium
1594
Maximum Non Negative Product in a Matrix	33.1%	Medium
2400
Number of Ways to Reach a Position After Exactly k Steps	33.0%	Medium
91
Decode Ways	32.7%	Medium
1986
Minimum Number of Work Sessions to Finish the Tasks	32.7%	Medium
5
Longest Palindromic Substring	32.4%	Medium
1981
Minimize the Difference Between Target and Chosen Elements	32.4%	Medium
1976
Number of Ways to Arrive at Destination	30.8%	Medium
464
Can I Win	29.7%	Medium
1654
Minimum Jumps to Reach Home	29.1%	Medium
2597
The Number of Beautiful Subsets	28.8%	Medium
2556
Disconnect Path in a Binary Matrix by at Most One Flip	28.4%	Medium
2310
Sum of Numbers With Units Digit K	25.8%	Medium
1191
K-Concatenation Maximum Sum	23.8%	Medium
2572
Count the Number of Square-Free Subsets	20.4%	Medium
