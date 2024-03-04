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


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        pass
