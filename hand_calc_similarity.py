# TODO: redesign similarity model
# TODO: hotkeys

qwerty_rows_right = [['Q', 'A', 'Z'],
                     ['W', 'S', 'X'],
                     ['E', 'D', 'C'],
                     ['R', 'F', 'V'],
                     ['T', 'G', 'B']]

qwerty_hotkeys = [['2', '5', '6'],
                  ['W', '5', '6'],
                  ['E', '3', '6'],
                  ['R', 'F', '6'],
                  ['T', '1', '2']]


def calc_similarity(hand, hand_ref):
    """
    >>> calc_similarity(convert_to_raw(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']), qwerty_rows_right)
    43
    """

    score = 0
    for i in range(5):
        for j in range(3):

            if hand[i][j] == 0:
                continue

            if hand[i][j] == hand_ref[i][j]:
                score += 10
                # ? if hotkey: score += 3
                continue

            if hand[i][j] in hand_ref[i]:
                score += 5
                continue

            row, col = get_index(hand_ref, hand[i][j])

            if row == -1:
                continue

            score += 2

    return score


def get_index(array, elem):
    for row, i in enumerate(array):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return row, column
    return -1, -1


def convert_to_raw(hand):
    hand_row = [[0,       hand[0], 0],
                [hand[4], hand[1], 0],
                [hand[5], hand[2], hand[6]],
                [hand[8], hand[3], hand[7]],
                [0,       hand[9], 0]]
    return hand_row


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    niro = ['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W']

    res = calc_similarity(convert_to_raw(aest), qwerty_rows_right)
    print(res)
