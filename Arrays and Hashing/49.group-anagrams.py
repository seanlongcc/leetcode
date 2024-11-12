#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

from typing import List
from collections import defaultdict
# @lc code=start


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # WALKCCC
        # create a list with a default value of a list for every key
        result = defaultdict(list)

        # iterate through each element in the list
        for str in strs:
            # the key is the string sorted, the value is a list of strings that when sorted, become the key
            key = ''.join(sorted(str))
            result[key].append(str)

        return list(result.values())

        # NEETCODE METHOD
        # result = defaultdict(list)
        # for s in strs:
        #     count = [0] * 26  # a ... z
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     result[tuple(count)].append(s)
        # return result.values()

        # MY FAILED ATTEMPT
        # anagrams = []
        # mapper = {}
        # for i in range(len(strs)):
        #     anagram_set = [strs[i]]
        #     for j in range(i+1, len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             anagram_set.append(strs[j])
        #     mapper[strs[i]] = anagram_set

        # anagrams.extend(mapper.values())

        # result = []
        # for i in anagrams:
        #     is_redundant = False
        #     for j in anagrams:
        #         if i == j:
        #             continue
        #         if set(i).issubset(set(j)):
        #             is_redundant = True
        #             break
        #     if not is_redundant:
        #         result.append(i)
        # return result

    # @lc code=end


Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
