# Leetcode 49. Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

# Example 1:

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create empty dictionary
        d = {}
        # convert each word into a key
        for s in strs:
            # add keys ( -> aet, ant, abt )
            key = "".join(sorted(s))
            if key in d:
                # append string into list; allows us to keep track of those
                # anagrams
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())


# This solution uses the defaultdict function.
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # alternative to Solution1: avoid having to check if key is in list and
        # if not, append
        d = defaultdict(list)

        for s in strs:
            key = "".join(sorted(list(s)))
            d[key].append(s)

        # we need to return the values as a list
        # either create a new list to be returned or use the list function as in
        # Solution1
        output = []
        for l in d.values():
            output.append(l)

        return output


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print("Solution 1:")
s = Solution()
print(s.groupAnagrams(strs))

print()

print("Solution 2:")
s = Solution2()
print(s.groupAnagrams(strs))

print()

print("Other examples:")
# Example 2:

strs = [""]
s = Solution()
# Output: [[""]]
print(s.groupAnagrams(strs))

# Example 3:

strs = ["a"]
s = Solution()
# Output: [["a"]]
print(s.groupAnagrams(strs))
