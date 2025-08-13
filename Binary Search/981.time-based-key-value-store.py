#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.store:
        #     self.store[key] = []

        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # Fetch the list of (timestamp, value) pairs for this key; [] if key not present.
        arr = self.store.get(key, [])

        # return "" if empty list
        if not arr:
            return ""

        # Set up binary search bounds over indices of arr.
        left, right = 0, len(arr) - 1

        # 'ans' holds the best candidate value seen so far where t <= timestamp.
        # If all stored timestamps are greater than 'timestamp', we will return "".
        ans = ""
        while left <= right:
            mid = (left + right) // 2
            # Unpack the (timestamp, value) at mid
            t, v = arr[mid]
            # Exact match: if we have a pair with t == timestamp, return immediately.
            if t == timestamp:
                return v

            # If the mid timestamp is less than the target time,
            # it's a valid candidate; record it and search to the right
            # for a possibly larger timestamp that’s still <= target.
            if t < timestamp:
                ans = v                 # best so far (≤ timestamp)
                left = mid + 1

            # Otherwise t > timestamp: search the left half.
            # we want t to be less than timestamp
            else:
                right = mid - 1
        return ans

        # Your TimeMap object will be instantiated and called as such:
        # obj = TimeMap()
        # obj.set(key,value,timestamp)
        # param_2 = obj.get(key,timestamp)
        # @lc code=end
