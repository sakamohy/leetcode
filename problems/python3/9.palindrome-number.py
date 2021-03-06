#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        temp = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10

        if temp == rev:
            return True
        else:
            return False

    def isPalindromeOther(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return False

        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x = x // 10

        return True if (x == reversedNum or x == reversedNum // 10) else False


# @lc code=end
