#DP Practice Set
#Ordered roughly easy -> hard. Try each one both top-down (memoization) and bottom-up (tabulation)
#like you did with fib in dp.py. Solve on paper first: define the state, the recurrence, and the base case(s)
#before you write any code. That's 90% of DP.


#=====================================================================
# 1. Climbing Stairs (warm-up, basically fib in disguise)
#=====================================================================
#You are climbing a staircase with n steps. Each time you can climb either 1 or 2 steps.
#How many distinct ways can you climb to the top?
#Example: n=4 -> 5 ways ([1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2])
#Hint: ways(n) = ways(n-1) + ways(n-2). Sound familiar?
#we need to find the number of ways to get to the top from the last 2 stairs because we can get to the current step from either of those
#the base case is when n=1 which is 1 and n=2 which is 2 becasue either 1 step twice or 2 steps once.
#It is the result of adding the last 2 steps because for example to get to step 3, it would be 1 + 2 since step 1 has 1 way and step 2 has 2 ways
#step 4 would be 2 + 3 
#going to use the memoization way--top to bottom "recursion with memorization" this will do most of the left subtree by hand and the rihgt tree will all be cache calls
def climb_stairs(n,cache=None):
    if cache is None:
        cache = {}
    if n==1:
        return 1
    if n==2:
        return 2
    if n in cache:
        return cache[n]
    cache[n] = climb_stairs(n-1, cache=cache) + climb_stairs(n-2,cache=cache)
    return cache[n]
print(climb_stairs(5))

#TABULATION--iterating with memory
def tabClimbStairs(n):
    if n==1:
        return 1
    if n==2:
        return 2
    dpMem = [0 for i in range(n+1)]
    dpMem[1] =1
    dpMem[2]=2
    for i in range(3, n+1):
        dpMem[i] = dpMem[i-2] + dpMem[i-1]#returns previous number of ways
    return dpMem[n]
print(tabClimbStairs(5))




#=====================================================================
# 2. House Robber
#=====================================================================
#Given a list of non-negative integers representing money at each house, find the max amount
#you can rob without robbing two ADJACENT houses.
#Example: [2,7,9,3,1] -> 12 (rob houses at index 0, 2, 4 -> 2+9+1)
#Hint: at each house you either skip it (take best up to i-1) or rob it (nums[i] + best up to i-2)
def house_robber(nums):
    pass


#=====================================================================
# 3. Coin Change (minimum coins)
#=====================================================================
#Given coin denominations and a target amount, return the fewest number of coins needed to make
#that amount. Return -1 if it can't be made.
#Example: coins=[1,2,5], amount=11 -> 3 (5+5+1)
#Hint: state = dp[amount] = min coins to make that amount. For each amount, try every coin.
def coin_change(coins, amount):
    pass


#=====================================================================
# 4. Longest Increasing Subsequence (LIS)
#=====================================================================
#Given an array of integers, find the length of the longest strictly increasing subsequence
#(doesn't have to be contiguous).
#Example: [10,9,2,5,3,7,101,18] -> 4 ([2,3,7,101] or [2,3,7,18])
#Hint: dp[i] = length of LIS ending exactly at index i. dp[i] = 1 + max(dp[j]) for all j<i where nums[j]<nums[i]
def longest_increasing_subsequence(nums):
    pass


#=====================================================================
# 5. 0/1 Knapsack
#=====================================================================
#Given item weights, item values, and a max capacity, find the max total value you can carry
#without exceeding capacity. Each item can only be used once (that's the "0/1" part).
#Example: weights=[1,3,4,5], values=[1,4,5,7], capacity=7 -> 9 (items with weight 3+4=7, value 4+5=9)
#Hint: 2D state - dp[i][c] = best value using first i items with capacity c.
#      Either skip item i, or take it (if it fits) and add value[i] + dp[i-1][c-weight[i]]
def knapsack_01(weights, values, capacity):
    pass


#=====================================================================
# 6. Longest Common Subsequence (LCS)
#=====================================================================
#Given two strings, find the length of their longest common subsequence.
#Example: "abcde", "ace" -> 3 ("ace")
#Hint: 2D state - dp[i][j] = LCS length of text1[:i] and text2[:j].
#      If chars match, dp[i][j] = 1 + dp[i-1][j-1]. Otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1])
def longest_common_subsequence(text1, text2):
    pass


#=====================================================================
# 7. Edit Distance (Levenshtein)
#=====================================================================
#Given two strings, find the minimum number of operations (insert, delete, replace) to convert
#word1 into word2.
#Example: "horse", "ros" -> 3 (horse -> rorse -> rose -> ros)
#Hint: similar 2D grid to LCS. If chars match, no cost, carry dp[i-1][j-1].
#      Otherwise 1 + min(insert, delete, replace) = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
def edit_distance(word1, word2):
    pass


#=====================================================================
# 8. Unique Paths (grid DP)
#=====================================================================
#A robot sits at the top-left corner of an m x n grid. It can only move right or down.
#How many unique paths are there to the bottom-right corner?
#Example: m=3, n=7 -> 28
#Hint: dp[r][c] = dp[r-1][c] + dp[r][c-1]. First row and first column are all 1s (only one way to get there)
def unique_paths(m, n):
    pass


#=====================================================================
# 9. Partition Equal Subset Sum
#=====================================================================
#Given a list of positive integers, determine if it can be partitioned into two subsets with
#equal sum.
#Example: [1,5,11,5] -> True ([1,5,5] and [11])
#Hint: this is 0/1 knapsack in disguise. Target = sum(nums)/2. Can we hit that target exactly
#      using a subset of nums? (If sum is odd, immediately False.)
def can_partition(nums):
    pass


#=====================================================================
# 10. Word Break
#=====================================================================
#Given a string s and a list of words (a dictionary), determine if s can be segmented into a
#space-separated sequence of one or more dictionary words.
#Example: s="leetcode", wordDict=["leet","code"] -> True
#Hint: dp[i] = True if s[:i] can be segmented. dp[0]=True (empty string).
#      dp[i] = True if there's some j<i where dp[j] is True AND s[j:i] is in the word set.
def word_break(s, word_dict):
    pass


