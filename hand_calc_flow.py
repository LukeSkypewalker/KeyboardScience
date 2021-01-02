import timeit
from data import bigrams_aestudcfgb


#       |1    |2    |3    |4    |5    |6    |7    |8    |9    |10
flow = [[   0,  0.9,  0.8, 0.85,  0.7,  0.6,  0.1,  0.2,  0.1,  0.2],  # 1
        [ 0.8,    0,  1.2,  0.9, -1.0,  1.1,  0.2,  0.4,  0.2,  0.1],  # 2
        [ 0.8,  0.9,    0,    3,  0.7, -0.6, -0.5,  0.4,  0.2,  0.1],  # 3
        [0.85,  0.8,  1.0,    0, 0.75,  0.9,  0.2, -0.5, -0.6, -0.6],  # 4
        [0.75, -1.0,  0.7,  0.7,    0,  0.6, -0.4,  0.1,  0.4,  0.1],  # 5
        [0.75,  0.4, -0.5,  1.1,  0.5,    0, -0.6,  0.2,  0.4,  0.1],  # 6
        [ 0.4,  0.3, -0.5,  0.4, -0.6, -1.0,    0,  0.7, -0.5,  0.1],  # 7
        [ 0.6,  0.4,  0.6, -0.5,  0.3,  0.3,  0.5,    0, -0.9, -1.0],  # 8
        [ 0.5,  0.4,  0.4, -0.6,  0.4,  0.5, -0.5, -1.0,    0, -1.0],  # 9
        [ 0.3,  0.1,  0.1, -1.0,  0.3,  0.1,  0.1, -1.0, -1.0,    0]]  # 10


def calc_flow(hand, bigrams):
    """
    >>> calc_flow(['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B'], bigrams_aestudcfgb)
    673711667.1999998
    """

    hand_flow_score = 0
    for b in bigrams:
        i = hand.index(b[0])
        j = hand.index(b[1])
        hand_flow_score += b[2] * flow[i][j]

    return hand_flow_score


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    print('flow_score', calc_flow(aest, bigrams_aestudcfgb))
    print('time', timeit.timeit('calc_flow(aest, bigrams_aest)', number=10,
                                setup="from __main__ import calc_flow, aest, bigrams_aest"))
