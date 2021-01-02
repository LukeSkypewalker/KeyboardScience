from math import factorial


def calc(num_of_keys):
    """
    >>> calc(20)
    184756.0
    >>> calc(22)
    705432.0
    >>> calc(26)
    10400600.0
    """
    left_hand = round(num_of_keys / 2)
    num_of_comb = factorial(num_of_keys) / (factorial(left_hand) * factorial(num_of_keys - left_hand))
    return num_of_comb


for i in range(8, 34):
    print(i, calc(i))
