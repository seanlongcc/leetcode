#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # my own extremely slow naive solution
        # result = []
        # if len(s) < len(p):
        #     return result
        # sorted_p = sorted(p)
        # for i in range(len(s) - len(p) + 1):
        #     if sorted_p == sorted(s[i:i+len(p)]):
        #         result.append(i)
        # return result

        s_length = len(s)
        p_length = len(p)

        # If the pattern is longer than the text, no matches are possible.
        if p_length > s_length:
            return []

        # target_counts: frequency of each character required by the pattern `p`
        # window_counts: frequency of each character in the current window of `s` (size == p_length)
        target_counts = {}
        window_counts = {}

        # Build initial counts for:
        # - the entire pattern `p`
        # - the first window of `s` of length `p_length` (i.e., s[0 : p_length])
        for i in range(p_length):
            target_counts[p[i]] = target_counts.get(p[i], 0) + 1
            window_counts[s[i]] = window_counts.get(s[i], 0) + 1

        # If the very first window matches the target counts, index 0 is a valid start
        result_indices = [0] if window_counts == target_counts else []

        # Sliding window boundaries: we will fix the window size to `p_length`
        window_start = 0  # start index of the current window

        # Extend the window to the right, one character at a time
        # `window_end` is the index of the new character entering the window
        for window_end in range(p_length, s_length):
            # 1) Add the incoming rightmost character
            window_counts[s[window_end]] = window_counts.get(
                s[window_end], 0) + 1

            # 2) Remove the outgoing leftmost character
            window_counts[s[window_start]] -= 1
            # Remove keys with zero count to keep dictionary equality checks simple and fast
            if window_counts[s[window_start]] == 0:
                window_counts.pop(s[window_start])

            # 3) Move the window forward by one (maintains window size == p_length)
            window_start += 1

            # 4) If the current window's counts match the target, record its start index
            if window_counts == target_counts:
                result_indices.append(window_start)

        return result_indices

        # @lc code=end
