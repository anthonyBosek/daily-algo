"""
    2416. Sum of Prefix Scores of Strings
    https://leetcode.com/problems/sum-of-prefix-scores-of-strings/

    You are given an array words of size n consisting of non-empty strings.

    We define the score of a string word as the number of strings words[i]
    such that word is a prefix of words[i].

    For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab"
    is 2, since "ab" is a prefix of both "ab" and "abc".

        - Return an array answer of size n where answer[i] is the sum of scores
            of every non-empty prefix of words[i].

    Note that a string is considered as a prefix of itself.

"""

from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        word_count = len(words)
        sorted_indices = sorted(range(word_count), key=lambda i: words[i])
        common_prefix_lengths = self._calculate_common_prefix_lengths(
            words, sorted_indices
        )
        scores = self._calculate_scores(words, sorted_indices, common_prefix_lengths)
        return scores

    def _calculate_common_prefix_lengths(self, words, sorted_indices):
        common_prefix_lengths = [0] * len(words)
        for i in range(1, len(words)):
            prev_word = words[sorted_indices[i - 1]]
            curr_word = words[sorted_indices[i]]
            common_length = 0
            while (
                common_length < len(prev_word)
                and common_length < len(curr_word)
                and prev_word[common_length] == curr_word[common_length]
            ):
                common_length += 1
            common_prefix_lengths[i] = common_length
        return common_prefix_lengths

    def _calculate_scores(self, words, sorted_indices, common_prefix_lengths):
        scores = [0] * len(words)
        for i, word_index in enumerate(sorted_indices):
            word_length = len(words[word_index])
            scores[word_index] += word_length
            j = i + 1
            common_length = word_length
            while j < len(words):
                common_length = min(common_length, common_prefix_lengths[j])
                if common_length == 0:
                    break
                scores[word_index] += common_length
                scores[sorted_indices[j]] += common_length
                j += 1
        return scores


#! Editortial
class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        # Initialize the root node of the trie.
        self.root = trie_node()

    # Insert function for the word.
    def insert(self, word):
        node = self.root
        for c in word:
            # If new prefix, create a new trie node.
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            # Increment the count of the current prefix.
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]

    # Calculate the prefix count using this function.
    def count(self, s):
        node = self.root
        ans = 0
        # The ans would store the total sum of counts.
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        # Insert words in trie.
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            # Get the count of all prefixes of given string.
            scores[i] = self.count(words[i])
        return scores
