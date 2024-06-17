"""
声明：
此题摘选自力扣：
https://leetcode.cn/problems/maximum-swap/description/

670. 最大交换

给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 10^8]
"""
import copy
from collections import defaultdict


class Solution:
    def maximumSwap_1(self, num: int) -> int:
        # 借用default dict
        list_num_res = copy.deepcopy(list(str(num)))
        list_num = copy.deepcopy(list(str(num)))
        list_num.sort(reverse=True)
        change_num = None
        change_index = 0
        num_dict = defaultdict(list)
        for index_num in range(len(list_num_res)):
            if not change_num and list_num_res[index_num] != list_num[index_num]:
                change_num = (list_num_res[index_num], list_num[index_num])
                change_index = index_num
            num_dict[list_num_res[index_num]].append(index_num)
        if change_num:
            list_num_res[change_index] = list_num[change_index]
            list_num_res[num_dict[change_num[1]][-1]] = change_num[0]
            return int(''.join(list_num_res))
        else:
            return num

    def maximumSwap(self, num: int) -> int:
        s = str(num)
        max_idx = len(s) - 1
        p = q = -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] > s[max_idx]:  # s[i] 是目前最大数字
                max_idx = i
            elif s[i] < s[max_idx]:  # s[i] 右边有比它大的
                p, q = i, max_idx  # 更新 p 和 q
        if p == -1:  # 这意味着 s 是降序的
            return num
        s = list(s)
        s[p], s[q] = s[q], s[p]  # 交换 s[p] 和 s[q]
        return int(''.join(s))


if __name__ == '__main__':
    S = Solution()
    print(S.maximumSwap(98368))
