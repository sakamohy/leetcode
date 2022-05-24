#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        z, p = 0, "I"
        for c in s[::-1]:
            z, p = z - d[c] if d[c] < d[p] else z + d[c], c

        return z


# @lc code=end
