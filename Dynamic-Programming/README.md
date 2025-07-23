# 动态规划题型总结 🧠📐

动态规划（Dynamic Programming）是 LeetCode 高频考点之一，适用于**最优子结构**和**重叠子问题**场景。常见模型有：

- 序列型DP（字符串/数组）
- 背包问题
- 匹配/结构判断
- 状态压缩

本节总结以下三道代表性动态规划题目：

- [1. 单词拆分（Word Break）](word-break.py)
- [2. 分割等和子集（Partition Equal Subset Sum）](partition-equal-subset-sum.py)
- [3. 最长有效括号（Longest Valid Parentheses）](longest-valid-parentheses.py)

---

## 1. 单词拆分（Word Break）

> LeetCode #139 - Medium  
> 题目链接：https://leetcode.com/problems/word-break/

### ✅ 思路

状态定义：  
- `dp[i]` 表示前 `i` 个字符 `s[:i]` 是否可以用字典中的单词拼出。

状态转移：
- 若存在某个 `j < i`，使得 `dp[j] == True` 且 `s[j:i]` 在字典中，则 `dp[i] = True`

### 🚀 解法步骤

1. 初始化 `dp[0] = True`（空串为有效）
2. 遍历 `i`，再枚举 `j`：
   - 若 `dp[j] == True` 且 `s[j:i] in wordDict`，则更新 `dp[i] = True`
3. 返回 `dp[len(s)]`

### ⏱️ 时间复杂度

- 时间：O(n²)（外层循环 * 字典查找）
- 空间：O(n)

### 🧠 关键点

- 动态规划 + 字符串切片
- 可以考虑将 wordDict 转为 set 以加快查找速度

---

## 2. 分割等和子集（Partition Equal Subset Sum）

> LeetCode #416 - Medium  
> 题目链接：https://leetcode.com/problems/partition-equal-subset-sum/

### ✅ 思路

该问题是 **0-1 背包问题** 的一个变种。

目标：判断是否可以从数组中选出若干个数，使其和为 `sum(nums) // 2`

状态定义：
- `dp[j]` 表示是否可以凑出和为 `j`

状态转移：
- `dp[j] = dp[j] or dp[j - num]`

遍历顺序：
- **倒序遍历**，防止同一轮内重复使用同一个数字

### 🚀 解法步骤

1. 判断总和是否为奇数，若是则直接返回 False
2. 初始化 `dp[0] = True`
3. 遍历每个数字 `num`：
   - 从 `target` 倒序到 `num`，更新 `dp[j]`
4. 返回 `dp[target]`

### ⏱️ 时间复杂度

- 时间：O(n * target)
- 空间：O(target)

### 🧠 关键点

- 背包问题状态压缩技巧：一维数组 + 倒序遍历
- 本质是是否能找到一组子集，其和等于 `sum(nums) // 2`

---

## 3. 最长有效括号（Longest Valid Parentheses）

> LeetCode #32 - Hard  
> 题目链接：https://leetcode.com/problems/longest-valid-parentheses/

### ✅ 思路

状态定义：
- `dp[i]` 表示以 `i` 结尾的最长有效括号子串长度

状态转移：
- 若 `s[i] == ')'` 且前一个是 `'('`，则：  
  `dp[i] = dp[i-2] + 2`
- 若 `s[i] == ')'` 且前一个是 `')'`，检查其前一个有效子串的前一位是否是 `'('`：  
  `dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]`

### 🚀 解法步骤

1. 初始化 `dp = [0] * n`
2. 从 i=1 开始遍历字符串：
   - 根据上述两种情况更新 dp[i]
3. 返回 `max(dp)`

### ⏱️ 时间复杂度

- 时间：O(n)
- 空间：O(n)

### 🧠 关键点

- DP 状态的含义是“以当前位置结尾的有效括号长度”
- 对于连续 `))`，需向前回溯查找是否能与 `(` 匹配

---

## 🧠 总结技巧

| 模型        | 应用题目 |
|-------------|----------|
| 序列型 DP   | Word Break、Longest Valid Parentheses |
| 背包问题    | Partition Equal Subset Sum、0-1 Knapsack |
| 匹配结构    | 括号匹配、正则匹配、子序列匹配等 |
| 状态压缩    | 用一维 `dp[]` 替代二维数组 |
| 倒序遍历    | 背包、滚动数组避免重复使用同一元素 |

---

👉 更多动态规划题型将持续补充，包括：

- 爬楼梯 / 打家劫舍
- 子序列（最长递增、公共子序列）
- 股票买卖系列
- 字符串编辑距离、回文子串等
