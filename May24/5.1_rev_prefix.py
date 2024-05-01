"""
    2000. Reverse Prefix of Word
    https://leetcode.com/problems/reverse-prefix-of-word/

    Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the
        first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

        - For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
            The resulting string will be "dcbaefd".

    Return the resulting string.

"""


def reversePrefix(word: str, ch: str) -> str:
    if ch in word:
        # i = word.index(ch)
        # return word[: i + 1][::-1] + word[i + 1 :]
        return word[: word.index(ch) + 1][::-1] + word[word.index(ch) + 1 :]
    return word

    # ? -----------------------------------------------

    #! cleanest
    # i = word.find(ch) + 1
    # return word[:i][::-1] + word[i:]

    # ? -----------------------------------------------

    #! my first attempt
    # i = word.find(ch)+1
    # pre = word[0:i]
    # cut = word[i:]
    # return pre[::-1]+cut

    # ? -----------------------------------------------

    #! slower & more memory
    # ci = -1
    # for i in range(len(word)):
    #     if word[i] == ch:
    #         ci = i
    #         break

    # if ci != -1:
    #     word = word[:i + 1][::-1] + word[i + 1:]

    # return word

    # ? -----------------------------------------------

    #! fancy
    #! Get prefix
    # try:
    #     prefix = word[:word.index(ch) + 1]
    #     reverse = prefix[::-1]
    #     return reverse + word[word.index(ch) + 1:]
    # except:
    #     return word
