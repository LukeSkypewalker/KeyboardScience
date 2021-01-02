from pprint import pprint

# TODO:
from hand_permutations import get_permutations

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    aest = ['A', 'E', 'S', 'T', 'U', 'D', 'C', 'F', 'G', 'B']
    pprint(get_permutations(aest))