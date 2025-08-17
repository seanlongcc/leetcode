#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        # Trim whitespace (both ends). If you want to match classic atoi more closely,
        # you could use s.lstrip() to remove only leading spaces.
        s = s.strip()
        if not s:
            return 0  # empty string -> 0

        # Determine the sign from the first character (default: +)
        sign = -1 if s[0] == '-' else 1
        # If there's an explicit sign, skip it
        if s[0] in {'-', '+'}:
            s = s[1:]

        num = 0

        # Consume consecutive digits and build the number
        for c in s:
            if not c.isdigit():
                break  # stop at first non-digit
            num = num * 10 + int(c)  # shift left (×10) and add current digit

            # Clamp on the fly to 32-bit signed range
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1

        # Apply sign and return
        return sign * num


# @lc code=end
Solution().myAtoi("1337c0d3")
