"""
    948. Bag of Tokens
    https://leetcode.com/problems/bag-of-tokens/

    You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens,
        where each tokens[i] donates the value of tokeni.

    Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed
        token in one of the two ways (but not both for the same token):

        - Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
        - Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.

    Return the maximum possible score you can achieve after playing any number of tokens.

"""

from collections import deque


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        deque = deque(tokens)
        while deque:
            if deque and power >= deque[0]:
                power -= deque.popleft()
                score += 1

            else:
                if len(deque) > 2 and score:
                    power += deque.pop()
                    score -= 1
                else:
                    return score

        return score

        # -----------------------------------------------------------

        # tokens.sort()
        # score = 0
        # max_score = 0
        # left = 0
        # right = len(tokens) - 1

        # while left <= right:
        #     if power >= tokens[left]:
        #         power -= tokens[left]
        #         left += 1
        #         score += 1
        #         max_score = max(max_score, score)
        #     elif score > 0:
        #         power += tokens[right]
        #         right -= 1
        #         score -= 1
        #     else:
        #         break

        # return max_score

        # -----------------------------------------------------------

        # tokens.sort()
        # score = 0
        # max_score = 0
        # i = 0
        # j = len(tokens) - 1
        # while i <= j:
        #     if power >= tokens[i]:
        #         power -= tokens[i]
        #         score += 1
        #         i += 1
        #         max_score = max(max_score, score)
        #     elif score > 0:
        #         power += tokens[j]
        #         score -= 1
        #         j -= 1
        #     else:
        #         break
        # return max_score
