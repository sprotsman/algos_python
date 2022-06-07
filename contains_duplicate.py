from typing import List

print("solution 1")


class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:    # py 3.5
        return len(set(nums)) != len(nums)


nums = [1, 2, 3, 1]

s1 = Solution1()
print(f"Duplicate in {nums} ? -> ", end=' ')
print(s1.containsDuplicate(nums))
# print(s1.containsDuplicate([1,2,3,1]))


print("\nsolution 2")


class Solution2:
    def containsDuplicate(self, nums: list[int]) -> bool:  # py 3.9+
        return len(set(nums)) != len(nums)


nums = [1, 2, 3, 5, 6]

s2 = Solution2()
print(f"Duplicate in {nums} ? -> ", end=' ')
print(s2.containsDuplicate(nums))


print("\nsolution 3")


class Solution3(object):
    def containsDuplicate(self, nums):
        return not len(nums) == len(set(nums))


s3 = Solution3()
print(s3.containsDuplicate([11, 2, 7, 2, 1, 8]))
print(s3.containsDuplicate([3, 4, 5, 6]))

print("\nsolution 4")

lst = [1, 2, 3, 3, 4]

if len(set(lst)) == len(lst):
    print("no duplicate")
else:
    print("duplicate found")

print("\nsolution 5")

planets = ['neptune', 'mars', 'saturn', 'earth']


def contains_duplicate(values):
    if len(values) != len(set(values)):
        return True
    else:
        return False


print(contains_duplicate(planets))

print("\nsolution 6")


def contains_duplicates(values):
    return len(values) != len(set(values))


print(contains_duplicates([5, 2, 4, 1, 4, 5]))  # -> True
print(contains_duplicates([7, 3, 2, 8, 9]))     # -> False
