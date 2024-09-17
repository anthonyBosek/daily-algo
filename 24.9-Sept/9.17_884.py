"""
    884. Uncommon Words from Two Sentences
    https://leetcode.com/problems/uncommon-words-from-two-sentences/

    A sentence is a string of single-space separated words where each word consists only of lowercase letters.

    A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

    Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

"""


class Solution:
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        from collections import Counter

        # Split the sentences into words and count their occurrences
        count = Counter(s1.split() + s2.split())

        # Filter and return the uncommon words
        return [word for word, freq in count.items() if freq == 1]


#! Approach 1: Counting
class Solution(object):
    def uncommonFromSentences(self, A, B):
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        # Alternatively:
        # count = collections.Counter(A.split())
        # count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]
