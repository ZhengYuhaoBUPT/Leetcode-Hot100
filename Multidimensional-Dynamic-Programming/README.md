# 多维动态规划题型总结 🧩📐

多维动态规划（二维 DP）适用于处理两个维度状态之间的关系，常见于**字符串比较**、**区间问题**、**状态依赖转移**等场景。

本节总结以下两道代表性二维动态规划题目：

- [1. 最长回文子串（Longest Palindromic Substring）](longest-palindromic-substring.py)
- [2. 最长公共子序列（Longest Common Subsequence）](longest-common-subsequence.py)

---

## 1. 最长回文子串（Longest Palindromic Substring）

> LeetCode #5 - Medium  
> 题目链接：https://leetcode.com/problems/longest-palindromic-substring/

### ✅ 思路

状态定义：  
- `dp[i][j]` 表示字符串 `s[i..j]` 是否为回文子串。

状态转移：
- 若 `s[i] != s[j]`，则 `dp[i][j] = False`
- 若 `s[i] == s[j]`，则：
  - 若 `j - i < 3`（子串长度 ≤ 3），直接判断为回文
  - 否则判断内部子串是否是回文：`dp[i][j] = dp[i+1][j-1]`

### 🚀 解法步骤

1. 初始化所有长度为 1 的子串为回文：`dp[i][i] = True`
2. 枚举子串右端点 `j`，再枚举左端点 `i < j`
3. 更新回文状态，并记录最长回文的位置
4. 返回最长回文子串

### ⏱️ 时间复杂度

- 时间：O(n²)
- 空间：O(n²)

### 🧠 关键点

- 中心扩展和动态规划都能解决本题
- 枚举顺序需保证状态转移时子状态已被计算（先 `j` 再 `i`）

---

## 2. 最长公共子序列（Longest Common Subsequence）

> LeetCode #1143 - Medium  
> 题目链接：https://leetcode.com/problems/longest-common-subsequence/

### ✅ 思路

状态定义：  
- `dp[i][j]` 表示字符串 `text1[:i]` 与 `text2[:j]` 的最长公共子序列长度。

状态转移：
- 如果 `text1[i-1] == text2[j-1]`，说明当前字符匹配：  
  `dp[i][j] = dp[i-1][j-1] + 1`
- 否则：  
  `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

### 🚀 解法步骤

1. 初始化二维数组 `dp`，大小为 `(m+1)*(n+1)`，全部为 0
2. 遍历字符串每个位置，更新公共子序列长度
3. 返回 `dp[m][n]` 即为最终结果

### ⏱️ 时间复杂度

- 时间：O(m * n)
- 空间：O(m * n)

### 🧠 关键点

- 匹配结构类 DP 的经典模型
- 可选优化：滚动数组压缩空间到 O(n)

---

## 🧠 总结技巧

| 模型类型     | 应用题目 |
|--------------|----------|
| 区间型 DP    | Longest Palindromic Substring（回文） |
| 字符串匹配   | Longest Common Subsequence（子序列） |
| 状态转移方向 | 由左上/左/上三种情况转移而来 |
| 二维空间优化 | 可压缩为滚动数组（适用于部分问题） |

---

👉 更多二维 DP 题型将持续补充，包括：

- 编辑距离
- 回文子序列
- 石子合并、戳气球等区间合并问题
