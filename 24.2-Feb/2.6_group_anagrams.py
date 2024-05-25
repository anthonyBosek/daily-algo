"""
    49. Group Anagrams
    https://leetcode.com/problems/group-anagrams/

    Given an array of strings strs, group the anagrams together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
        typically using all the original letters exactly once.

"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]
        return list(anagrams.values())

    # -------------------------------------------------------------------------

    # def getSignature(self, s: str) -> str:
    #     count = [0] * 26
    #     for c in s:
    #         count[ord(c) - ord('a')] += 1

    #     result = []
    #     for i in range(26):
    #         if count[i] != 0:
    #             result.extend([chr(i + ord('a')), str(count[i])])

    #     return ''.join(result)

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     result = []
    #     groups = defaultdict(list)

    #     for s in strs:
    #         groups[self.getSignature(s)].append(s)
