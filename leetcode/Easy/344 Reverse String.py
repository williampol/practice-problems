"""
--- Description ---

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        # 1
        """
        for n in range(len(s)-1):
            popped = s.pop(0)
            s.insert(len(s)-n, popped)
        """

        # 2
        for x in range(len(s)//2):
            s[x], s[-x-1] = s[-x-1], s[x]

"""
--- Submission ---

1.
Runtime: 1174 ms, faster than 5.04% of Python3 online submissions for Reverse String.
Memory Usage: 18.5 MB, less than 45.70% of Python3 online submissions for Reverse String.

2.
Runtime: 256 ms, faster than 73.52% of Python3 online submissions for Reverse String.
Memory Usage: 18.4 MB, less than 86.20% of Python3 online submissions for Reverse String.
"""