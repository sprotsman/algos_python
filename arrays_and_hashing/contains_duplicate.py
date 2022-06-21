# Leetcode 271. Contains Duplicate

from typing import List

print("solution 1")

# py 3.5: 'List' requires import


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


nums = [1, 2, 3, 1]

s1 = Solution1()
print(f"Duplicate in {nums} ? -> ", end=' ')
print(s1.containsDuplicate(nums))


print("\nsolution 2")


# py 3.9+
class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:  # py 3.9+
        return len(set(nums)) != len(nums)


nums = [1, 2, 3, 5, 6]

s2 = Solution2()
print(f"Duplicate in {nums} ? -> ", end=' ')
print(s2.containsDuplicate(nums))


print("\nsolution 3")


class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


s3 = Solution3()
print(s3.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(s3.containsDuplicate([1, 2, 3, 4]))


print("\nsolution 4")

lst = [1, 2, 3, 3, 4]

if len(set(lst)) == len(lst):
    print("no duplicate")
else:
    print("duplicate found")
