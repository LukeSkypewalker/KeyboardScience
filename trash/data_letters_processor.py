from data import *


def calc_letter_freq(letter, bigrams):
    """
    >>> calc_letter_freq('E', bigrams26)
    1031369703
    >>> calc_letter_freq('A', bigrams26)
    739408216
    """
    return sum(b[2] for b in get_all_bigrams_for_letter(letter, bigrams))
    # return sum(b[2] for b in bigrams if letter in (b[0], b[1]))


def calc_letters_freq(letters, bigrams):
    """
    >>> calc_letters_freq(('E','A'), bigrams26) #doctest: +NORMALIZE_WHITESPACE
    [('E', 1031369703),
     ('A', 739408216)]
    """
    return [(letter, calc_letter_freq(letter, bigrams)) for letter in letters]


def get_all_bigrams_for_letter(letter, bigrams):
    """
    >>> get_all_bigrams_for_letter('E', bigrams8) #doctest: +NORMALIZE_WHITESPACE
    [['E', 'R', 77134382],
     ['R', 'E', 60923600],
     ['E', 'S', 57070453],
     ['E', 'N', 48991276],
     ['E', 'A', 43329810],
     ['T', 'E', 42295813],
     ['E', 'T', 32872552],
     ['S', 'E', 31532272],
     ['N', 'E', 27331675],
     ['E', 'E', 18497942],
     ['E', 'I', 16026915],
     ['E', 'O', 13524186],
     ['I', 'E', 12505546],
     ['O', 'E', 2616308],
     ['A', 'E', 815963]]
    """
    return [b for b in bigrams if letter in (b[0], b[1])]


def get_bigram_list_summarized(_letter, bigrams):
    """
    >>> get_bigram_list_summarized('E', bigrams26) #doctest: +NORMALIZE_WHITESPACE
    [['R', 138058, [['E', 'R', 77134382], ['R', 'E', 60923600]]],
     ['H', 108248, [['H', 'E', 100689263], ['E', 'H', 7559141]]],
     ['S', 88603, [['E', 'S', 57070453], ['S', 'E', 31532272]]],
     ['N', 76323, [['E', 'N', 48991276], ['N', 'E', 27331675]]],
     ['T', 75168, [['T', 'E', 42295813], ['E', 'T', 32872552]]],
     ['D', 73678, [['E', 'D', 46647960], ['D', 'E', 27029835]]],
     ['L', 53476, [['L', 'E', 30383262], ['E', 'L', 23092248]]],
     ['C', 45579, [['E', 'C', 25775798], ['C', 'E', 19803619]]],
     ['M', 45383, [['M', 'E', 27237733], ['E', 'M', 18145294]]],
     ['A', 44146, [['E', 'A', 43329810], ['A', 'E', 815963]]],
     ['V', 39895, [['V', 'E', 29320973], ['E', 'V', 10574011]]],
     ['P', 29598, [['P', 'E', 15573318], ['E', 'P', 14024377]]],
     ['B', 29207, [['B', 'E', 19468489], ['E', 'B', 9738798]]],
     ['I', 28532, [['E', 'I', 16026915], ['I', 'E', 12505546]]],
     ['W', 27962, [['E', 'W', 14776406], ['W', 'E', 13185116]]],
     ['G', 22711, [['G', 'E', 14425023], ['E', 'G', 8286463]]],
     ['F', 21782, [['E', 'F', 13252227], ['F', 'E', 8529289]]],
     ['O', 16140, [['E', 'O', 13524186], ['O', 'E', 2616308]]],
     ['Y', 14028, [['E', 'Y', 7528342], ['Y', 'E', 6499305]]],
     ['K', 13062, [['K', 'E', 10650670], ['E', 'K', 2411639]]],
     ['U', 8602, [['U', 'E', 4927837], ['E', 'U', 3674130]]],
     ['X', 6303, [['E', 'X', 5649363], ['X', 'E', 653947]]],
     ['J', 2744, [['J', 'E', 1487348], ['E', 'J', 1256993]]],
     ['Z', 2175, [['Z', 'E', 1709871], ['E', 'Z', 465466]]],
     ['Q', 1467, [['E', 'Q', 1461436], ['Q', 'E', 6020]]]]
    """

    data = get_all_bigrams_for_letter(_letter, bigrams)
    bidirect_digrams = []
    for letter in letters26:
        if letter == _letter:
            continue
        bs = ([b for b in data if letter in (b[0], b[1])])
        bsum = round(sum([b[2] for b in bs]) / 1000)
        bidirect_digrams.append([letter, bsum, bs])

    bidirect_digrams.sort(key=lambda x: x[1], reverse=True)
    return bidirect_digrams


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # check letters frequencies
    letters_freq = calc_letters_freq(letters26, bigrams26)
    letters_freq.sort(key=lambda x: x[1], reverse=True)
    print(*letters_freq, sep='\n')

    # data = get_all_letters_bigrams('A', bigrams)
    # data.sort(key=lambda x: x[2], reverse=True)
    # print(*(data), sep='\n')

    # data = [get_bigram_list_summarized(letter, bigrams) for letter in letters26]
    # from pprint import pprint
    # pprint(data)
