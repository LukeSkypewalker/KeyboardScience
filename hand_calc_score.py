from hand_calc_balance import calc_disbalance_fingers
from hand_calc_flow import calc_flow


def calc_hand_score(hand, bigrams10):
    """
    >>> calc_hand_score(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'])
    2871427583.9803076
    >>> calc_hand_score(['S', 'N', 'R', 'H', 'D', 'L', 'C', 'M', 'F', 'W'])
    2661701034.507109

    >>> calc_hand_score(['E', 'A', 'O', 'I', 'T', 'P', 'Y', 'G', 'U', 'B'])
    2719305440.718976
    >>> calc_hand_score(['O', 'R', 'I', 'N', 'L', 'H', 'Y', 'M', 'P', 'W'])
    2801934941.2619944
    """

    flow = calc_flow(hand, bigrams10)
    disbalance = calc_disbalance_fingers(hand)
    score = flow / disbalance
    return score
