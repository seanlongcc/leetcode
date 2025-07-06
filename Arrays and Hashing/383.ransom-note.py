#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # my unefficient method that i needed help to complete with the right logic tho
        # mag_map = {}
        # for letter in magazine:
        #     mag_map[letter] = mag_map.get(letter, 0) + 1

        # note_map = {}
        # for letter in ransomNote:
        #     note_map[letter] = note_map.get(letter, 0) + 1

        # for char, needed in note_map.items():
        #     if mag_map.get(char, 0) < needed:
        #         return False
        # return True
        # ---------------

        # Build a frequency map of all letters available in the magazine
        mag_count = Counter(magazine)

        # Iterate through the ransom note and check character counts
        for char in ransomNote:
            # check if the magazine still has at least one of that letter
            if mag_count.get(char, 0) > 0:
                mag_count[char] -= 1
            else:
                return False
        return True

        # @lc code=end
Solution().canConstruct(ransomNote="aa", magazine="aab")
