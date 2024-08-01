"""
    2678. Number of Senior Citizens
    https://leetcode.com/problems/number-of-senior-citizens/

    You are given a 0-indexed array of strings details. Each element of details provides information
    about a given passenger compressed into a string of length 15. The system is such that:

        • The first ten characters consist of the phone number of passengers.
        • The next character denotes the gender of the person.
        • The following two characters are used to indicate the age of the person.
        • The last two characters determine the seat allotted to that person.

    Return the number of passengers who are strictly more than 60 years old.

"""


def countSeniors(details):
    #! --- my one liner solution ---
    return len([d for d in details if int(d[11:13]) > 60])

    #! --- my original solution ---
    # oldies = 0
    # for passenger in details:
    #     phone_number = passenger[0:9]
    #     gender = passenger[10]
    #     age = int(passenger[11:13])
    #     seat = passenger[13:]
    #     print(phone_number, gender, age, seat)
    #     if age > 60:
    #         oldies += 1

    # return oldies

    #! --- refactor solution ---

    # ct = 0
    # for d in details:
    #     if int(d[11:13]) > 60:
    #         ct += 1
    # return ct
