"""
    2225. Find Players With Zero or One Losses
    https://leetcode.com/problems/find-players-with-zero-or-one-losses/

    You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

    Return a list answer of size 2 where:

    • answer[0] is a list of all players that have not lost any matches.
    • answer[1] is a list of all players that have lost exactly one match.
    The values in the two lists should be returned in increasing order.

    Note:

    • You should only consider the players that have played at least one match.
    • The testcases will be generated such that no two matches will have the same outcome.
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # my solution
        pass

        # leetcode solution
        # zeroLoss, oneLoss, moreLoss = set(), set(), set()

        # for match in matches:
        #     winner, loser = match[0], match[1]

        #     # Add winner.
        #     if winner not in oneLoss and winner not in moreLoss:
        #         zeroLoss.add(winner)

        #     # Add or move loser.
        #     if loser in zeroLoss:
        #         zeroLoss.remove(loser)
        #         oneLoss.add(loser)
        #     elif loser in oneLoss:
        #         oneLoss.remove(loser)
        #         moreLoss.add(loser)
        #     elif loser in moreLoss:
        #         continue
        #     else:
        #         oneLoss.add(loser)

        # answer = [sorted(list(zeroLoss)), sorted(list(oneLoss))]
        # return answer

        # copilot solution
        # winners = set()
        # losers = set()
        # for match in matches:
        #     winners.add(match[0])
        #     losers.add(match[1])
        # return [sorted(list(winners - losers)), sorted(list(losers - winners))]


matches = [
    [1, 2],
    [2, 3],
    [1, 4],
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 8],
    [5, 9],
    [6, 10],
    [8, 11],
    [9, 11],
    [10, 11],
]
print(Solution().findWinners(matches))
# matches = [[0,1],[1,2],[2,3],[3,4]]
# print(Solution().findWinners(matches))
# matches = [[1,2],[2,3]]
# print(Solution().findWinners(matches))
