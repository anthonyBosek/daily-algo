"""
    205. Isomorphic Strings
    https://leetcode.com/problems/isomorphic-strings/

    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the order of characters.
    
    No two characters may map to the same character, but a character may map to itself.

"""


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s = list(s)
    t = list(t)
    if len(set(s)) != len(set(t)):
        return False
    d1 = {}
    for i in range(len(s)):
        d1[s[i]] = t[i]
    print(d1)
    for i in range(len(s)):
        s[i] = d1[s[i]]
    return True if s == t else False

    # ----------------------------------------------

    # map = {}
    # map2 = {}
    # for i in range(len(s)):
    #     if s[i] in map:
    #         if map[s[i]] != t[i]:
    #             return False
    #     if t[i] in map2:
    #         if map2[t[i]] != s[i]:
    #             return False
    #     else:
    #         map[s[i]] = t[i]
    #         map2[t[i]] = s[i]
    # return True

    # ----------------------------------------------

    # if len(s) != len(t):
    #     return False
    # s_dict = {}
    # t_dict = {}
    # for i in range(len(s)):
    #     if s[i] not in s_dict:
    #         s_dict[s[i]] = t[i]
    #     if t[i] not in t_dict:
    #         t_dict[t[i]] = s[i]
    #     if s_dict[s[i]] != t[i] or t_dict[t[i]] != s[i]:
    #         return False
    # return True
