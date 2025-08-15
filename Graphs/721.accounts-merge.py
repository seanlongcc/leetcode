#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

from collections import defaultdict
# @lc code=start


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # lmao did the wrong problem
        # result = defaultdict(set)
        # for account in accounts:
        #     if account[0] not in result.keys():
        #         result[account[0]].update(account[1:])
        #     else:
        #         for email in account[1:]:
        #             result[account[0]].add(email)
        # print(result)
        # rows = []

        # for name, emails in result.items():
        #     row = [name]
        #     row.extend(emails)
        #     rows.append(row)

        # return rows

        # @lc code=end
