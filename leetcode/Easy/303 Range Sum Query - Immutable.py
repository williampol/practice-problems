# type:ignore
"""
--- Description ---

Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between 
  indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""

# We have to instantiate the class in this problem as well
# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums
        

#     def sumRange(self, left: int, right: int) -> int:
#         return sum(self.nums[left:right+1])


# The other solutions used a method called prefix sum which is way faster
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefixSum.append(self.prefixSum[i-1]+nums[i])
    
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        return self.prefixSum[right] - self.prefixSum[left-1]

"""
--- Submission ---

1.
Runtime: 1163 ms, faster than 34.75% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.5 MB, less than 69.56% of Python3 online submissions for Range Sum Query - Immutable.

2.
Runtime: 71 ms, faster than 99.80% of Python3 online submissions for Range Sum Query - Immutable.
Memory Usage: 17.7 MB, less than 62.07% of Python3 online submissions for Range Sum Query - Immutable.
"""