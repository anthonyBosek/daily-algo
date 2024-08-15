"""
    860. Lemonade Change
    https://leetcode.com/problems/lemonade-change/

    At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order
    one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with
    either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net
    transaction is that the customer pays $5.

    Note that you do not have any change in hand at first.

    Given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can
    provide every customer with the correct change, or false otherwise.

"""


def lemonadeChange(bills):
    """
    :type bills: List[int]
    :rtype: bool
    """
    pass
    # Count of $5 and $10 bills in hand
    five_dollar_bills = 0
    ten_dollar_bills = 0

    # Iterate through each customer's bill
    for customer_bill in bills:
        if customer_bill == 5:
            # Just add it to our count
            five_dollar_bills += 1
        elif customer_bill == 10:
            # We need to give $5 change
            if five_dollar_bills > 0:
                five_dollar_bills -= 1
                ten_dollar_bills += 1
            else:
                # Can't provide change, return false
                return False
        else:  # customer_bill == 20
            # We need to give $15 change
            if ten_dollar_bills > 0 and five_dollar_bills > 0:
                # Give change as one $10 and one $5
                five_dollar_bills -= 1
                ten_dollar_bills -= 1
            elif five_dollar_bills >= 3:
                # Give change as three $5
                five_dollar_bills -= 3
            else:
                # Can't provide change, return false
                return False
    # If we've made it through all customers, return true
    return True
