"""
522. 最长特殊序列 II
给定字符串列表 strs ，返回其中 最长的特殊序列 的长度。如果最长特殊序列不存在，返回 -1 。
特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 s 的 子序列可以通过删去字符串 s 中的某些字符实现。

例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。

示例 1：
输入: strs = ["aba","cdc","eae"]
输出: 3

示例 2:
输入: strs = ["aaa","aaa","aa"]
输出: -1

提示:
2 <= strs.length <= 50
1 <= strs[i].length <= 10
strs[i] 只包含小写英文字母

声明：
此题摘选自力扣： https://leetcode.cn/problems/longest-uncommon-subsequence-ii/?envType=daily-question&envId=2024-06-17
"""
import re


class Solution:

    def format_str(self, str_num, _list_):
        # 正则判断是否包含
        s = ""
        for s_ in _list_[str_num]:
            s_ = s_ + "(.*?)"
            s += s_
        s = "(.*?)" + s
        s_len = []
        for str_num_ in range(len(_list_)):
            if str_num_ == str_num:
                continue
            elif _list_[str_num_] == _list_[str_num]:
                return None
            elif re.findall(s, _list_[str_num_]):
                return None
            else:
                s_len.append(len(_list_[str_num]))
        return max(s_len)

    def check(self, s: str, t: str):
        # 枚举
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def findLUSlength(self, strs: list[str]) -> int:
        res = []
        for str_num in range(len(strs)):
            if r := self.format_str(str_num, strs):
                res.append(r)
        return max(res) if res else -1

    def findLUSlength_2(self, strs: list[str]) -> int:
        ans = -1
        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if i != j and self.check(s, t):
                    break
            else:
                ans = max(ans, len(s))
        return ans


if __name__ == '__main__':
    S = Solution()
    print(S.findLUSlength(["aaa", "aaa", "aa"]))
    print(S.findLUSlength(["aba", "cdc", "eae"]))
    print(S.findLUSlength(["aabbcc", "aabbcc", "cb"]))
