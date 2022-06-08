# Leetcode 1. Two Sum

# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

# You can return the answer in any order.

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map = {}  # dict of val:index

        for i, num in enumerate(nums):
            difference = target - num

            # Is the difference in the map?
            if difference in map:
                # If yes, return the index of difference (val) from the map and
                # the index.
                return [map[difference], i]
            # If not, add it to the map.
            map[num] = i


nums = [2, 7, 11, 15]
target = 9

s = Solution()
print(s.twoSum(nums, target))  # [0, 1]

nums = [2, 3, 6, 8]
target = 9

s = Solution()
print(s.twoSum(nums, target))  # [1, 2]

nums = [3, 3]
target = 6

s = Solution()
print(s.twoSum(nums, target))  # [0, 1]
