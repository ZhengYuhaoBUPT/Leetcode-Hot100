# 哈希表题型总结 🧠🔍

哈希表是一类极其高效的查找结构，适用于大多数需要 **快速查找、去重、分组统计、前后关联信息匹配** 等题型。通过 `dict`、`set`、`defaultdict` 等形式灵活应用，在 LeetCode Hot 100 中也频频出现。

本节总结以下典型哈希题：

- [1. 两数之和 (Two Sum)](two-sum.py)
- [2. 字母异位词分组 (Group Anagrams)](group-anagrams.py)
- [3. 最长连续序列 (Longest Consecutive Sequence)](longest-consecutive-sequence.py)

---

## 1. 两数之和

> LeetCode #1 - Easy  
> 题目链接：https://leetcode.com/problems/two-sum/

### ✅ 思路

利用哈希表记录遍历过的元素，边遍历边判断当前数 `num` 的补数 `target - num` 是否在哈希表中出现过。

### 🚀 解法步骤

1. 初始化一个空哈希表 `hashtable = {}`
2. 遍历数组：
   - 若 `target - num` 存在于哈希表中，直接返回索引对 `[hashtable[target - num], i]`
   - 否则将当前数及其下标加入哈希表

### ⏱️ 时间复杂度

- 时间：O(n)
- 空间：O(n)

### 🧠 关键点

- 哈希表用于存储**值 -> 索引**的映射
- 一边查找一边插入，避免两次遍历

---

## 2. 字母异位词分组

> LeetCode #49 - Medium  
> 题目链接：https://leetcode.com/problems/group-anagrams/

### ✅ 思路

异位词排序后是相同的字符串。将排序后的字符串作为哈希表的键，把原始字符串分组加进去。

### 🚀 解法步骤

1. 初始化 `defaultdict(list)`
2. 遍历字符串数组：
   - 对每个字符串进行排序：`key = ''.join(sorted(s))`
   - 将原字符串加入以 `key` 为键的列表中
3. 返回所有哈希表中的分组结果

### ⏱️ 时间复杂度

- 时间：O(n * klogk)（n为字符串数量，k为单个字符串长度）
- 空间：O(nk)

### 🧠 关键点

- 字符串排序作为哈希表键
- 使用 `collections.defaultdict(list)` 避免 key 初始化

---

## 3. 最长连续序列

> LeetCode #128 - Hard  
> 题目链接：https://leetcode.com/problems/longest-consecutive-sequence/

### ✅ 思路

将所有数放入 `set` 中，查找 **每个数作为序列起点时能延伸出的最长连续子序列**。

### 🚀 解法步骤

1. 将数组转为 `set(nums)` 以便 O(1) 查找
2. 遍历 set：
   - 若 `num - 1` 不在集合中，说明是一个新的起点
   - 向右延伸：判断 `num + 1`, `num + 2`, ... 是否在 set 中，更新序列长度
3. 记录最长长度并返回

### ⏱️ 时间复杂度

- 时间：O(n)
- 空间：O(n)

### 🧠 关键点

- 利用 `set` 做快速存在性判断
- 只有当 `num-1` 不在 set 时才尝试延伸，**避免重复计算**

---

## 🧠 总结技巧

| 技巧/思路           | 说明 |
|----------------------|------|
| 补数查找             | 如 Two Sum，利用哈希表存储值到索引 |
| 排序作为哈希键       | 如 Group Anagrams，异位词统一表示 |
| 集合去重 + 延伸判断   | 如 Longest Consecutive Sequence，只从起点开始判断连续性 |
| `defaultdict`        | 自动初始化嵌套列表，适合分组统计 |
| `set()`              | 快速去重、判断存在性 |

---

👉 更多哈希表相关题型将在后续更新中持续补充，比如：

- 子串类问题（滑动窗口 + 哈希）
- 哈希 + 数学映射（如同余判断）
- 双哈希技巧（如字符串编码）

