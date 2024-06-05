"""
    1002. Find Common Characters
    https://leetcode.com/problems/find-common-characters/

    Given a string array words, return an array of all characters that show up in all strings
    within the words (including duplicates). You may return the answer in any order.

"""

from collections import Counter


def commonChars(words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    if len(words) < 2:
        return words
    res = []
    word1 = set(words[0])
    for char in word1:
        frq = min([word.count(char) for word in words])
        res += [char] * frq
    return res

    # ------------------------------------

    # arr = []
    # l = set(words[0])
    # for i in l:
    #     t = min(w.count(i) for w in words)
    #     arr += [i] * t
    # return arr

    # ------------------------------------

    # if not words:
    #     return []
    # res = Counter(words[0])
    # for word in words[1:]:
    #     res &= Counter(word)
    # return list(res.elements())
