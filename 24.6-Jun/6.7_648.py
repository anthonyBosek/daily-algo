"""
    648. Replace Words
    https://leetcode.com/problems/replace-words/

    In English, we have a concept called root, which can be followed by some other word to form another
    longer word - let's call this word derivative. For example, when the root "help" is followed by the
    word "ful", we can form a derivative "helpful".

    Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces,
    replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced
    by more than one root, replace it with the root that has the shortest length.

    Return the sentence after the replacement.

"""

from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for letter in word:
                if letter in node:
                    node = node[letter]
                else:
                    new_node = {}
                    node[letter] = new_node
                    node = new_node
            else:
                node["is_word"] = True

        words = []
        for word in sentence.split(" "):
            node = trie
            for idx, letter in enumerate(word):
                if letter in node:
                    node = node[letter]
                    if node.get("is_word"):
                        words.append(word[: idx + 1])
                        break
                else:
                    words.append(word)
                    break
            else:
                words.append(word)

        return " ".join(words)


##! ===============================================================================================
##! 2nd Approach
# class Solution_0:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         s = set(dictionary)
#         sentence = sentence.split()
#         for j, w in enumerate(sentence):
#             for i in range(1, len(w)):
#                 if w[:i] in s:
#                     sentence[j] = w[:i]
#                     break
#         return " ".join(sentence)


# class Solution_1:
#     def replaceWords(self, roots, sentence):
#         rootset = set(roots)

#         def replace(word):
#             for i in range(1, len(word)):
#                 if word[:i] in rootset:
#                     return word[:i]
#             return word

#         return " ".join(map(replace, sentence.split()))


# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         d = {w: len(w) for w in dictionary}
#         mi, ma = min(d.values()), max(d.values())
#         wrds = sentence.split()
#         res = []
#         for w in wrds:
#             c = w
#             for i in range(mi, min(ma, len(w)) + 1):
#                 ss = w[:i]
#                 if ss in d:
#                     c = ss
#                     break
#             res.append(c)
#         return " ".join(res)


##! ===============================================================================================
##! 3rd Approach
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False


# class Trie:
#     def __init__(self):
#         self.root = TrieNode()

#     def insert(self, word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True

#     def search_shortest_prefix(self, word):
#         node = self.root
#         prefix = ""
#         for char in word:
#             if char not in node.children:
#                 break
#             node = node.children[char]
#             prefix += char
#             if node.is_end_of_word:
#                 return prefix
#         return word


# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         trie = Trie()
#         for root in dictionary:
#             trie.insert(root)

#         words = sentence.split()

#         result = []

#         for word in words:
#             result.append(trie.search_shortest_prefix(word))

#         return " ".join(result)
