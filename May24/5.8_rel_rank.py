"""
    506. Relative Ranks
    https://leetcode.com/problems/relative-ranks/

    You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition.
    All the scores are guaranteed to be unique.

    The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place
    athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

        - The 1st place athlete's rank is "Gold Medal".
        - The 2nd place athlete's rank is "Silver Medal".
        - The 3rd place athlete's rank is "Bronze Medal".
        - For the 4th place to the nth place athlete, their rank is their placement number
            (i.e., the xth place athlete's rank is "x").

    Return an array answer of size n where answer[i] is the rank of the ith athlete.

"""

from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """
        This function takes a list of integers and returns a list of strings.
        The function uses a dictionary to store the score and index of the athletes.
        The dictionary is then sorted in reverse order of scores.
        The function then assigns ranks to the athletes based on their index.
        The ranks are stored in a list and returned.
        """
        score_dict = {score[i]: i for i in range(len(score))}
        score_dict = dict(sorted(score_dict.items(), reverse=True))
        ranks = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i, key in enumerate(score_dict.keys()):
            if i < 3:
                score[score_dict[key]] = ranks[i]
            else:
                score[score_dict[key]] = str(i + 1)
        return score

        # ---------------------------------------------------------------------------------------------

        # # Sort the score in descending order
        # sorted_score = sorted(score, reverse=True)

        # # Create a dictionary to store the rank of each athlete
        # rank = {}

        # # Assign the rank to each athlete
        # for i in range(len(sorted_score)):
        #     if i == 0:
        #         rank[sorted_score[i]] = "Gold Medal"
        #     elif i == 1:
        #         rank[sorted_score[i]] = "Silver Medal"
        #     elif i == 2:
        #         rank[sorted_score[i]] = "Bronze Medal"
        #     else:
        #         rank[sorted_score[i]] = str(i + 1)

        # # Return the rank of each athlete
        # return [rank[score[i]] for i in range(len(score))]

        # ----------------------------------------------------------------------------------------------

        # N = len(score)

        # # Save the index of each athelete
        # score_to_index = defaultdict(int)
        # for i in range(N):
        #     score_to_index[score[i]] = i

        # # Sort score in descending order
        # score.sort(reverse=True)

        # # Assign ranks to athletes
        # rank = [" "] * N
        # for i in range(N):
        #     if i == 0:
        #         rank[score_to_index[score[i]]] = "Gold Medal"
        #     elif i == 1:
        #         rank[score_to_index[score[i]]] = "Silver Medal"
        #     elif i == 2:
        #         rank[score_to_index[score[i]]] = "Bronze Medal"
        #     else:
        #         rank[score_to_index[score[i]]] = str(i + 1)

        # return rank

        # ----------------------------------------------------------------------------------------------

        # sorted_score = sorted(score, reverse=True)
        # rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i+1) for i in range(3, len(score))]
        # rank_dict = {sorted_score[i]: rank[i] for i in range(len(score))}
        # return [rank_dict[s] for s in score]
