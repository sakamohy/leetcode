#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        m = {"(": ")", "[": "]", "{": "}"}
        stuck = []
        for c in s:
            if c in m.keys():
                stuck.append(c)
                continue
            if len(stuck) == 0 or m.get(stuck.pop()) != c:
                return False

        return len(stuck) == 0


# @lc code=end
