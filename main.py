from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from itertools import combinations

from combination_processor import process_combination
from data import freq, letters18, bigrams18


# Let's sort all letters by frequency and split them to "top 8 for home row positions" and "other".
# We will take all combinations of 4 from top_frequency letters and mix them with combinations of non-top letters
# to form all relevant left-hand combinations of layout.
#
# TODO get rid of magic numbers and hardcode. everything seems to be hardcoded to letters18
def get_combinations(letters_set):
    letters = sorted(letters_set, key=lambda letter: freq[letter], reverse=True)
    combs = []
    letters_homerow = letters[0:9]
    letters_other = letters[9:]
    for top4 in list(combinations(letters_homerow, 4)):
        for others in list(combinations(letters_other, 5)):
            comb = list(top4 + others)
            combs.append(comb)
    return combs


# Main program
if __name__ == '__main__':
    letters = letters18
    bigrams = bigrams18

    # Get all relevant left-hand combinations
    combs = get_combinations(letters)

    # Calc combinations scores
    time_start = datetime.now()
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(process_combination, left_hand, bigrams, letters) for left_hand in combs]
    result = [future.result() for future in futures]
    time_end = datetime.now()
    print('time', time_end - time_start)

    result.sort(key=lambda x: x[2], reverse=True)
    # pprint([future.result() for future in futures])
    print(*result, sep='\n')

    with open('output.txt', 'w') as file:
        file.write('\n'.join('%s %s %s' % x for x in result))
