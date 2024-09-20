"""
    214. Shortest Palindrome
    https://leetcode.com/problems/shortest-palindrome/

    You are given a string s. You can convert s to a palindrome by adding characters in front of it.

    Return the shortest palindrome you can find by performing this transformation.
    
"""


def shortestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return s

    # Create a new string that is the original string plus a separator and the reverse of the original string
    new_s = s + "#" + s[::-1]
    n = len(new_s)

    # Create a list to store the length of the longest prefix which is also a suffix
    lps = [0] * n

    # Build the LPS array
    for i in range(1, n):
        j = lps[i - 1]
        while j > 0 and new_s[i] != new_s[j]:
            j = lps[j - 1]
        if new_s[i] == new_s[j]:
            j += 1
        lps[i] = j

    # The length of the longest palindromic prefix
    longest_palindromic_prefix_length = lps[-1]

    # The characters to add in front of the original string to make it a palindrome
    chars_to_add = s[longest_palindromic_prefix_length:][::-1]

    return chars_to_add + s

    # # -------------------------------------------------------------------------------

    # rev_s = s[::-1]
    # # Concatenate s and rev_s with a special character in between
    # new_s = s + "#" + rev_s
    # # Create a list to store the length of the longest prefix which is also a suffix
    # lps = [0] * len(new_s)

    # # Build the LPS array
    # j = 0
    # for i in range(1, len(new_s)):
    #     while j > 0 and new_s[i] != new_s[j]:
    #         j = lps[j - 1]
    #     if new_s[i] == new_s[j]:
    #         j += 1
    #         lps[i] = j

    # # The length of the longest palindromic prefix
    # longest_palindromic_prefix_length = lps[-1]

    # # The characters to add in front of s to make it a palindrome
    # chars_to_add = rev_s[: len(s) - longest_palindromic_prefix_length]

    # # Return the shortest palindrome
    # return chars_to_add + s


#! Approach 1: Brute Force
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        reversed_string = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""


#! Approach 2: Two Pointer *** best approach ***
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return s

        # Find the longest palindromic prefix
        left = 0
        for right in range(length - 1, -1, -1):
            if s[right] == s[left]:
                left += 1

        # If the whole string is a palindrome, return the original string
        if left == length:
            return s

        # Extract the suffix that is not part of the palindromic prefix
        non_palindrome_suffix = s[left:]
        reverse_suffix = non_palindrome_suffix[::-1]

        # Form the shortest palindrome by prepending the reversed suffix
        return (
            reverse_suffix + self.shortestPalindrome(s[:left]) + non_palindrome_suffix
        )


#! Approach 3: KMP (Knuth-Morris-Pratt) Algorithm
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Reverse the original string
        reversed_string = s[::-1]

        # Combine the original and reversed strings with a separator
        combined_string = s + "#" + reversed_string

        # Build the prefix table for the combined string
        prefix_table = self._build_prefix_table(combined_string)

        # Get the length of the longest palindromic prefix
        palindrome_length = prefix_table[-1]

        # Construct the shortest palindrome by appending the reverse of the suffix
        suffix = reversed_string[: len(s) - palindrome_length]
        return suffix + s

    # Helper function to build the KMP prefix table
    def _build_prefix_table(self, s: str) -> list:
        prefix_table = [0] * len(s)
        length = 0

        # Build the table by comparing characters
        for i in range(1, len(s)):
            while length > 0 and s[i] != s[length]:
                length = prefix_table[length - 1]
            if s[i] == s[length]:
                length += 1
            prefix_table[i] = length
        return prefix_table


#! Approach 4: Rolling Hash Based Algorithm
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        hash_base = 29
        mod_value = int(1e9 + 7)
        forward_hash = 0
        reverse_hash = 0
        power_value = 1
        palindrome_end_index = -1

        # Calculate rolling hashes and find the longest palindromic prefix
        for i, current_char in enumerate(s):
            # Update forward hash
            forward_hash = (
                forward_hash * hash_base + (ord(current_char) - ord("a") + 1)
            ) % mod_value

            # Update reverse hash
            reverse_hash = (
                reverse_hash + (ord(current_char) - ord("a") + 1) * power_value
            ) % mod_value
            power_value = (power_value * hash_base) % mod_value

            # If forward and reverse hashes match, update palindrome end index
            if forward_hash == reverse_hash:
                palindrome_end_index = i

        # Find the remaining suffix after the longest palindromic prefix
        suffix = s[palindrome_end_index + 1 :]

        # Reverse the remaining suffix
        reversed_suffix = suffix[::-1]

        # Prepend the reversed suffix to the original string and return the result
        return reversed_suffix + s


#! Approach 5: Manacher's Algorithm
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Return early if the string is null or empty
        if not s:
            return s

        # Preprocess the string to handle palindromes uniformly
        modified_string = self._preprocess_string(s)
        n = len(modified_string)
        palindrome_radius_array = [0] * n
        center = 0
        right_boundary = 0
        max_palindrome_length = 0

        # Iterate through each character in the modified string
        for i in range(1, n - 1):
            mirror_index = 2 * center - i

            # Use previously computed values to avoid redundant calculations
            if right_boundary > i:
                palindrome_radius_array[i] = min(
                    right_boundary - i, palindrome_radius_array[mirror_index]
                )

            # Expand around the current center while characters match
            while (
                modified_string[i + 1 + palindrome_radius_array[i]]
                == modified_string[i - 1 - palindrome_radius_array[i]]
            ):
                palindrome_radius_array[i] += 1

            # Update the center and right boundary if the palindrome extends beyond the current boundary
            if i + palindrome_radius_array[i] > right_boundary:
                center = i
                right_boundary = i + palindrome_radius_array[i]

            # Update the maximum length of palindrome starting at the beginning
            if i - palindrome_radius_array[i] == 1:
                max_palindrome_length = max(
                    max_palindrome_length, palindrome_radius_array[i]
                )

        # Construct the shortest palindrome by reversing the suffix and prepending it to the original string
        suffix = s[max_palindrome_length:][::-1]
        return suffix + s

    def _preprocess_string(self, s: str) -> str:
        # Add boundaries and separators to handle palindromes uniformly
        return "^" + "#" + "#".join(s) + "#$"
