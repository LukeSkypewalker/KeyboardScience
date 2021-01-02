from data import freq


# TODO: redesign balance coefficient ?

fingers_balance_reference = [8, 11, 15, 15]

#
# def calc_disbalance_total(left_hand, right_hand):
#     balance_fingers_left = calc_disbalance_fingers(left_hand)
#     balance_fingers_right = calc_disbalance_fingers(right_hand)
#     balance_hand = calc_disbalance_hands(left_hand)
#     balance = balance_fingers_left + balance_fingers_right + balance_hand
#     return max(balance, 1)


# def calc_disbalance_hand(hand):
#     balance_fingers_left = calc_balance_fingers(hand)
#     balance_hand = calc_balance_hands(hand)
#     balance = balance_fingers_left + + balance_hand
#     return max(balance, 1)


def calc_fingers_rows(hand):
    """
    >>> calc_fingers_rows(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'])
    [8.04, 15.22, 13.67, 15.030000000000001]
    >>> calc_fingers_rows(['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    [7.64, 10.350000000000001, 14.280000000000001, 13.56]
    """

    rows = [freq[hand[0]],
            freq[hand[1]] + freq[hand[4]],
            freq[hand[2]] + freq[hand[5]] + freq[hand[6]],
            freq[hand[3]] + freq[hand[7]] + freq[hand[8]]]  # + freq[hand[9]
    return rows


def calc_disbalance_fingers(_hand):
    """
    >>> calc_disbalance_fingers(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'])
    1.0562
    >>> calc_disbalance_fingers(['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    1.0317
    """
    fingers_row = calc_fingers_rows(_hand)
    deviation = [abs(a - b) for a, b in zip(fingers_balance_reference, fingers_row)]
    disbalance = 1 + 0.01 * sum(deviation)
    return disbalance


def calc_disbalance_hands(hand):
    s = 0
    for letter in hand:
        s += freq[letter]
    deviation = abs(50 - 1.095 - s)
    disbalance = 1 + 0.01 * deviation
    return disbalance


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    print('left', calc_fingers_rows(aest))
    print('right', calc_fingers_rows(niro))

    print('left sum', calc_disbalance_fingers(aest))
    print('right sum', calc_disbalance_fingers(niro))

    print('balance hands', calc_disbalance_hands(aest))
