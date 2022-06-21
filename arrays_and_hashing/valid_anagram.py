# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.

from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashmap = dict()

        if len(s) != len(t):
            return False

        for i in s:
            if i in hashmap:
                # if char(i) is already in hashmap, increment counter by 1
                hashmap[i] += 1
            # if this is the first time we are seeing char(i), then add it to
            # hashmap
            else:
                hashmap[i] = 1

        for i in t:
            if i in hashmap:
                # if char(i) is already in hashmap, decrement counter by 1
                hashmap[i] -= 1
            # if this is the first time we are seeing char(i), add it to hashmap
            else:
                hashmap[i] = 1

        # if any of the entries in hashmap are NOT 0 then we do not have an
        # anagram
        for i in hashmap:
            if hashmap[i] != 0:
                return False

        return True


s = "anagram"
t = "nagaram"

s1 = Solution()
print(s1.isAnagram(s, t))

s = "rat"
t = "car"

s1 = Solution()
print(s1.isAnagram(s, t))


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count_s, count_t = {}, {}  # create two empty dictionaries (hashmaps)

        for i in range(len(s)):
            # Build the dictionaries
            # if char exists, increment count by 1 (use get method (0 default value)
            # because the first time through the key won't be in the dictionary)
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_s[t[i]] = 1 + count_s.get(t[i], 0)

        # Are the counts the same?
        for k in count_s:
            if count_s[k] != count_t.get(k, 0):
                return False

        return True


s2 = Solution2()
print(s2.isAnagram(s, t))


class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


s3 = Solution3()
print(s3.isAnagram(s, t))


class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = ''.join(sorted(s))
        sort_t = ''.join(sorted(t))

        if sort_s != sort_t:
            return False

        return True


s = "anagram"
t = "gramana"

s4 = Solution4()
print(s4.isAnagram(s, t))


class Solution5:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s5 = Solution5()
print(s5.isAnagram(s, t))
