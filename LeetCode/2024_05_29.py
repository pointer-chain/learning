"""
2981. 找出出现至少三次的最长特殊子字符串 I
给你一个仅由小写英文字母组成的字符串 s 。
如果一个字符串仅由单一字符组成，那么它被称为 特殊 字符串。例如，字符串 "abc" 不是特殊字符串，而字符串 "ddd"、"zz" 和 "f" 是特殊字符串。
返回在 s 中出现 至少三次 的 最长特殊子字符串 的长度，如果不存在出现至少三次的特殊子字符串，则返回 -1 。
子字符串 是字符串中的一个连续 非空 字符序列。

示例 1：
输入：s = "aaaa"
输出：2
解释：出现三次的最长特殊子字符串是 "aa" ：子字符串 "aaaa"、"aaaa" 和 "aaaa"。
可以证明最大长度是 2 。

示例 2：
输入：s = "abcdef"
输出：-1
解释：不存在出现至少三次的特殊子字符串。因此返回 -1 。

示例 3：
输入：s = "abcaba"
输出：1
解释：出现三次的最长特殊子字符串是 "a" ：子字符串 "abcaba"、"abcaba" 和 "abcaba"。
可以证明最大长度是 1 。

提示：
3 <= s.length <= 50
s 仅由小写英文字母组成。
"""
from collections import defaultdict


class Solution:
    def maximumLength(self, s: str) -> int:
        strut_res = defaultdict(list)
        count_num = 0
        for i, s_i in enumerate(s):
            count_num += 1
            if i + 1 == len(s) or s_i != s[i + 1]:
                strut_res[s_i].append(count_num)  # 统计连续字符长度
                count_num = 0
        # 至少三次的做法
        ans = 0
        for a in strut_res.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

        K = 4
        # 至少K次的做法
        ans = 0
        for a in strut_res.values():
            a.sort(reverse=True)
            a.extend([0, 0])  # 假设还有两个空串
            ans = max(ans, a[0] - K + 1, min(a[0] - K + 1 + 1, a[1]), a[2])
        return ans if ans else -1


if __name__ == '__main__':
    """输入和输出"""
    # 确定输入条件：s、小写、3~50位
    # 确定输出： 不存在-1， 存在返回最大长度
    S = Solution()
    S.maximumLength(s="abcabaasadadsaadsqaasdqwsaadwqaa")
