"""
    1684. Count the Number of Consistent Strings
    https://leetcode.com/problems/count-the-number-of-consistent-strings/

    You are given a string allowed consisting of distinct characters and an array of strings words.
    A string is consistent if all characters in the string appear in the string allowed.

    Return the number of consistent strings in the array words.

"""


class Solution:
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(allowed)
        count = 0
        for word in words:
            if all(char in allowed for char in word):
                count += 1
        return count


#! Approach 1: Brute Force
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_word_consistent = True

            # Check each character in the current word
            for char in word:
                is_char_allowed = False

                # Check if the current character is in the allowed string
                for allowed_char in allowed:
                    if allowed_char == char:
                        is_char_allowed = True
                        break  # Character found, no need to continue searching

                # If the character is not allowed, mark the word as inconsistent
                if not is_char_allowed:
                    is_word_consistent = False
                    break  # No need to check remaining characters

            # If the word is consistent, increment the count
            if is_word_consistent:
                consistent_count += 1

        return consistent_count


#! Approach 2: Boolean Array
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a boolean list to mark which characters are allowed
        is_allowed = [False] * 26

        # Mark all characters in 'allowed' as True in the is_allowed list
        for char in allowed:
            is_allowed[ord(char) - ord("a")] = True

        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_consistent = True

            # Check each character of the current word
            for char in word:
                # If any character is not allowed, mark as inconsistent and break
                if not is_allowed[ord(char) - ord("a")]:
                    is_consistent = False
                    break

            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1

        return consistent_count


#! Approach 3: Hash Set
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a set to store the allowed characters
        allowed_chars = set(allowed)

        consistent_count = 0

        # Iterate through each word in the 'words' list
        for word in words:
            # Check if all characters in the word are in allowed_chars
            if all(char in allowed_chars for char in word):
                consistent_count += 1

        # Return the total count of consistent strings
        return consistent_count


#! Approach 4: Bit Manipulation
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Create a bitmask representing the allowed characters
        allowed_bits = 0

        # Set the corresponding bit for each character in allowed
        for char in allowed:
            allowed_bits |= 1 << (ord(char) - ord("a"))

        consistent_count = 0

        # Iterate through each word in the words list
        for word in words:
            is_consistent = True

            # Check each character in the word
            for char in word:
                # Calculate the bit position for the current character
                bit = (allowed_bits >> (ord(char) - ord("a"))) & 1

                # If the bit is 0, the character is not allowed
                if not bit:
                    is_consistent = False
                    break

            # If the word is consistent, increment the count
            if is_consistent:
                consistent_count += 1

        return consistent_count


#! ??? Fast ???
import json
import sys
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        occur = [False] * 26
        count = 0

        for c in allowed:
            occur[ord(c) - ord("a")] = True

        for word in words:
            if self.check(word, occur):
                count += 1

        return count

    def check(self, word: str, occur: List[bool]) -> bool:
        for c in word:
            if not occur[ord(c) - ord("a")]:
                return False
        return True


def kdsmain():
    input_data = sys.stdin.read().strip().split("\n")
    results = []

    i = 0
    while i < len(input_data):
        allowed = json.loads(input_data[i])
        words = json.loads(input_data[i + 1])
        result = Solution().countConsistentStrings(allowed, words)
        results.append(result)
        i += 2

    with open("user.out", "w") as f:
        for result in results:
            f.write(f"{result}\n")


if __name__ == "__main__":
    kdsmain()
    exit(0)
