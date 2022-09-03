"""
--- Description ---

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        x = s
        while x:
            print(x)
            if not x[0] in x[1:]:
                return s.index(x[0])
            x = [i for i in x if i != x[0]]
            if len(x) == 1:
                return s.index(x[0])

        return -1

obj = Solution()
print(obj.firstUniqChar("aabb"))

"""
--- Submission ---

Runtime: 719 ms, faster than 11.15% of Python3 online submissions for First Unique Character in a String.
Memory Usage: 14.7 MB, less than 6.52% of Python3 online submissions for First Unique Character in a String.
"""