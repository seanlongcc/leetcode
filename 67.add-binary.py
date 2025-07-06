#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_rev = a[::-1]
        b_rev = b[::-1]
        carry = 0
        result_bits = []

        # Iterate up to the longer length
        max_len = max(len(a_rev), len(b_rev))
        for i in range(max_len):
            # Get the i-th bit of each (or 0 if past the end)
            # checks if out of bound, if not, then just use a/b_rev[i] as the value
            bit_a = int(a_rev[i]) if i < len(a_rev) else 0
            bit_b = int(b_rev[i]) if i < len(b_rev) else 0

            total = bit_a + bit_b + carry

            # Compute the bit for this position: if total is even, bit is 0; if odd, bit is 1
            result_bits.append(str(total % 2))
            # Compute the carry for the next position: if total ≥ 2, carry is 1; otherwise it’s 0
            carry = total // 2

        # If there’s a leftover carry, append it
        if carry:
            result_bits.append('1')

    # Reverse back to MSB-first and join
    return ''.join(result_bits[::-1])
    # @lc code=end
