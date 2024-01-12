def halvesAreAlike(self, s: str) -> bool:
    low = s.lower()
    vwls = set("aeiou")
    half = len(low) // 2
    first = low[half:]
    second = low[:half]
    first_count = 0
    second_count = 0
    for i in range(half):
        if first[i] in vwls:
            first_count += 1
        if second[i] in vwls:
            second_count += 1

    return first_count == second_count
