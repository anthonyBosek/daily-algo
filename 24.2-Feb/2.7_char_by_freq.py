"""
    451. Sort Characters By Frequency
    https://leetcode.com/problems/sort-characters-by-frequency/

    Given a string s, sort it in decreasing order based on the frequency of the characters.
    
    The frequency of a character is the number of times it appears in the string.

    Return the sorted string. If there are multiple answers, return any of them.

"""


def frequencySort(s):
    # my solution
    #
    # creat dict for character frequency
    freq = {}

    # iterate through string and increment frequency count
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    # use dict.items to create (key,value) tuple and sort by frequencies - descending
    s_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # concatenate charcters onto result string
    result = ""
    for char, count in s_freq:
        result += char * count

    return result

    # ---------------------------------------------------------------

    # # Step 1: Count the frequency of each character
    # char_count = Counter(s)

    # # Step 2: Sort characters based on their frequency in descending order
    # sorted_chars = sorted(char_count, key=char_count.get, reverse=True)

    # # Step 3: Build the result string by repeating characters according to their frequency
    # result = ''
    # for char in sorted_chars:
    #     result += char * char_count[char]

    # # Step 4: Return the final sorted string
    # return result

    # ---------------------------------------------------------------

    # counter = Counter(s)
    # pq = [(-freq, char) for char, freq in counter.items()]
    # heapq.heapify(pq)
    # result = ''
    # while pq:
    #     freq, char = heapq.heappop(pq)
    #     result += char * -freq
    # return result

    # ---------------------------------------------------------------

    # copilot solution
    # freq = {}
    # for c in s:
    #     if c in freq:
    #         freq[c] += 1
    #     else:
    #         freq[c] = 1

    # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # result = ""
    # for c, count in sorted_freq:
    #     result += c * count

    # return result

    # ---------------------------------------------------------------

    # s = sorted(s, reverse=True)
    # return "".join(sorted(s, key=lambda k: s.count(k), reverse=True))


print(frequencySort("tree"))  # "eert"
print(frequencySort("cccaaa"))  # "cccaaa"
print(frequencySort("Aabb"))  # "bbAa"
print(frequencySort("loveleetcode"))  # "eeeeoollvtdc"
print(frequencySort("raaeaedere"))  # "eeeeaaarrd"
