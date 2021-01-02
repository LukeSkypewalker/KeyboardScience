from datetime import datetime
from hand_calc_balance import calc_disbalance_hands
from hand_permutations import calc_best_permutation
from data import *


# Sum frequency if letters are in different hands
def calc_handswitching_score(left_hand_comb, bigrams):
    return sum(b[2] for b in bigrams if (b[0] in left_hand_comb) != (b[1] in left_hand_comb))


def process_combination(left_hand, bigrams, letters):
    hand_switch_score = calc_handswitching_score(left_hand, bigrams)
    right_hand = [letter for letter in letters if letter not in left_hand]
    right_hand.sort(key=lambda letter: freq[letter], reverse=True)
    best_right = calc_best_permutation(right_hand, bigrams)
    best_left = calc_best_permutation(left_hand, bigrams)
    disbalance_hands = calc_disbalance_hands(left_hand)
    score = round((hand_switch_score + best_left[1] + best_right[1])/disbalance_hands)
    return best_left[0], best_right[0], score


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aestudcfgb = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']

    time_start = datetime.now()
    res = process_combination(aestudcfgb, bigrams20, letters20)
    print(res)
    time_end = datetime.now()
    print('time', time_end - time_start)