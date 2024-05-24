"""
    1255. Maximum Score Words Formed by Letters
    https://leetcode.com/problems/maximum-score-words-formed-by-letters/

    Given a list of words, list of single letters (might be repeating) and score of every character.

    Return the maximum score of any valid set of words formed by using the given letters
    (words[i] cannot be used two or more times).

    It is not necessary to use all characters in letters and each letter can only be used once.
    Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

"""


class Solution:
    def maxScoreWords(self, words, letters, score):
        """
        words: List[str]
        letters: List[str]
        score: List[int]
        rtype: int
        """
        # Count the frequency of each letter in letters
        freq = [0] * 26
        for letter in letters:
            freq[ord(letter) - ord("a")] += 1

        # Initialize the score of each word
        word_score = [0] * len(words)
        for i, word in enumerate(words):
            for letter in word:
                word_score[i] += score[ord(letter) - ord("a")]

        # Recursive function to get the maximum score
        def dfs(i):
            if i == len(words):
                return 0
            # Skip the current word
            skip = dfs(i + 1)
            # Check if we can use the current word
            can_use = True
            for letter in words[i]:
                freq[ord(letter) - ord("a")] -= 1
                if freq[ord(letter) - ord("a")] < 0:
                    can_use = False
            if can_use:
                use = word_score[i] + dfs(i + 1)
            else:
                use = 0
            # Restore the frequency of each letter
            for letter in words[i]:
                freq[ord(letter) - ord("a")] += 1
            return max(skip, use)

        return dfs(0)

        # ? -------------------------------------------------------------------------
        #
        ## --- solution from leetcode ---
        #
        # scores = [0 for i in range(len(words))]
        # word_score = [0 for i in range(len(words))]
        # letters_freq = [0 for i in range(26)]
        # for letter in letters:
        #     letters_freq[ord(letter) - ord("a")] += 1

        # for idx in range(len(words)):
        #     word = words[idx]
        #     for c in word:
        #         code = ord(c) - ord("a")
        #         if letters_freq[code] > 0:
        #             word_score[idx] += score[code]
        #         else:
        #             word_score[idx] = -1
        #             break

        # state = set()

        # def backtrack(word_idx, score, permutation_key, l_freq):
        #     permutation_key |= 1 << word_idx

        #     if word_idx == len(words):
        #         return

        #     if permutation_key in state:
        #         return

        #     if word_score[word_idx] == -1:
        #         return

        #     for i in range(26):
        #         if l_freq[i] > letters_freq[i]:
        #             return

        #     state.add(permutation_key)
        #     score += word_score[word_idx]
        #     scores[word_idx] = max(scores[word_idx], score)

        #     for idx in range(word_idx + 1, len(words)):
        #         for c in words[idx]:
        #             code = ord(c) - ord("a")
        #             l_freq[code] += 1

        #         backtrack(idx, score, permutation_key, l_freq)

        #         for c in words[idx]:
        #             code = ord(c) - ord("a")
        #             l_freq[code] -= 1

        # result = 0

        # for idx in range(len(words)):
        #     l_freq = [0 for i in range(26)]

        #     for c in words[idx]:
        #         code = ord(c) - ord("a")
        #         l_freq[code] += 1

        #     permutation_key = 1 << idx
        #     backtrack(idx, 0, permutation_key, l_freq)
        #     result = max(result, scores[idx])

        # return result
