# Leetcode 347. Top K Frequent Elements
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
# Example 1:
#
# 1 and 2 appear the most in this list:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
#
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

import heapq
from itertools import count
from typing import Counter, List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Make a dictionary with all of the ints as keys and the values being
        # the number of times it appears. How many times does each number appear
        # in the list?
        c = Counter(nums)
        answer = []
        mk = c.most_common(k)

        for key in range(len(mk)):
            answer.append(mk[key][0])

        return answer


s = Solution()

nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1, 2]
print("Solution1:")
print(s.topKFrequent(nums, k))

nums = [1]
k = 1
# Output: [1]
print(s.topKFrequent(nums, k))

nums = [4, 1, -1, 2, -1, 2, 3]
k = 2
# Output: [-1, 2]
print(s.topKFrequent(nums, k))


# Using heap
class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using heap
        c = Counter(nums)
        # Convert into a list
        # Make value negative because we want this to be a max heap
        c = [(-v, k) for k, v in c.items()]
        # heapify this
        heapq.heapify(c)
        output = []
        for _ in range(k):
            # pop off item
            item = heapq.heappop(c)
            # append key into our output
            output.append(item[1])
        return output


nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1, 2]
s = Solution2()
print("Solution2:")
print(s.topKFrequent(nums, k))


# using heap nlargest
class Solution3:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        # pick n largest elements from heap, pass keys of count and pick k
        # largest from it, and pass key
        return heapq.nlargest(k, c.keys(), key=c.get)


nums = [1, 1, 2, 2, 2, 3, 5, 5, 5, 5, 5]
k = 2
# Output: [5, 2]
s = Solution3()
print("Solution3:")
print(s.topKFrequent(nums, k))
