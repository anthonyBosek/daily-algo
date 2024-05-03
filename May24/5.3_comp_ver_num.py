"""
    165. Compare Version Numbers
    https://leetcode.com/problems/compare-version-numbers/

    Given two version numbers, version1 and version2, compare them.

    Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain
    leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the
    leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are
    valid version numbers.

    To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer
    value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does
    not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than
    version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

    Return the following:

        - If version1 < version2, return -1.
        - If version1 > version2, return 1.
        - Otherwise, return 0.

"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        for i in range(max(len(v1), len(v2))):
            n1 = v1[i] if i < len(v1) else 0
            n2 = v2[i] if i < len(v2) else 0

            if n1 < n2:
                return -1
            elif n1 > n2:
                return 1

        return 0

        # ---------------------------------------------------------

        # v1 = list(map(int, version1.split('.')))
        # v2 = list(map(int, version2.split('.')))

        # if len(v1) < len(v2):
        #     v1 += [0] * (len(v2) - len(v1))
        # elif len(v2) < len(v1):
        #     v2 += [0] * (len(v1) - len(v2))

        # for i in range(len(v1)):
        #     if v1[i] > v2[i]:
        #         return 1
        #     elif v1[i] < v2[i]:
        #         return -1

        # return 0

        # ---------------------------------------------------------

        # version1 = list(map(int, version1.split(".")))
        # version2 = list(map(int, version2.split(".")))

        # for i, j in zip(version1, version2):
        #     if i < j:
        #         return -1
        #     if i > j:
        #         return 1

        # ret = 1
        # if len(version1) == len(version2):
        #     return 0
        # elif len(version1) < len(version2):
        #     ret = -1
        #     version1, version2 = version2, version1

        # if all(x == 0 for x in version1[len(version2):]):
        #     return 0
        # return ret
