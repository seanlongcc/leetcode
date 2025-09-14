#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # MY BRUTE FORCE
        # def is_palindrome(sub: str) -> bool:
        #     left, right = 0, len(sub) - 1
        #     while left < right:
        #         if sub[left] != sub[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True

        # length = len(s)
        # longest = ""

        # for i in range(length):
        #     # Outer prune: no room to beat current best
        #     if length - i <= len(longest):
        #         break

        #     # Inner loop still your idea, but we break early when we can
        #     for j in range(length):  # (you can keep this)
        #         left = i
        #         right = length - j  # shrinks as j grows

        #         # If window can't beat current best, no point continuing (right only shrinks)
        #         if right - left <= len(longest):
        #             break

        #         if right <= left:
        #             break  # invalid/empty window, nothing longer remains for this i

        #         sub = s[left:right]

        #         if is_palindrome(sub):
        #             # longest for this i found (we're shrinking), so stop
        #             longest = sub
        #             break

        # return longest

        # OPTIMIZED

        def expand(l: int, r: int) -> str:
            """
            Expand pointers outward from a chosen 'center' while the substring remains a palindrome.
            - For odd-length palindromes, start with l == r (centered on a character).
            - For even-length palindromes, start with r == l + 1 (centered between two chars).
            Returns the maximal palindromic slice s[l':r'] discovered.
            """
            # Grow while indices are in bounds AND mirrored characters match.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            # We've stepped one past the last valid matching pair on both sides,
            # so the palindrome is the slice just inside those pointers.
            return s[l + 1: r]

        # Initialize with any single character (a length-1 palindrome).
        longest = s[0]

        # Try every possible center once.
        for i in range(len(s)):
            # Odd-length: center at s[i]
            p1 = expand(i, i)
            if len(p1) > len(longest):
                longest = p1

            # Even-length: center between s[i] and s[i+1]
            p2 = expand(i, i + 1)
            if len(p2) > len(longest):
                longest = p2

        return longest

        # @lc code=end
