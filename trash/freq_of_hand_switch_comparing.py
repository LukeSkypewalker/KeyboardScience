from trash.combs_sum import *
from data import *

aset = ('Q', 'D', 'F', 'P', 'K',
        'A', 'S', 'E', 'T', 'G',
        'Z', 'X', 'C', 'V', 'B')

aest = ('Q', 'U', 'D', 'G', 'K',
        'A', 'E', 'S', 'T', 'J',
        'X', 'C', 'F')

aest2 = ('Q', 'U', 'D', 'F', 'K',
         'A', 'E', 'S', 'T', 'G',
         'X', 'C', 'V')

qwerty = ('Q', 'W', 'E', 'R', 'T',
          'A', 'S', 'D', 'F', 'G',
          'Z', 'X', 'C', 'V', 'B')

workman = ('Q', 'D', 'R', 'W', 'B',
           'A', 'S', 'H', 'T', 'G',
           'Z', 'X', 'M', 'C', 'V')

norman = ('Q', 'W', 'D', 'F', 'K',
          'A', 'S', 'E', 'T', 'G',
          'Z', 'X', 'C', 'V', 'B')

stnr = ('S', 'T', 'N', 'R', 'L', 'D', 'C', 'M', 'F', 'P', 'W', 'B', 'V')
snrh = ('S', 'N', 'R', 'H', 'L', 'D', 'C', 'M', 'F', 'P', 'W', 'B', 'V')

combs = (aset, qwerty, aest, aest2, norman, workman, stnr, snrh)

comb_sum = calc_combs_sums(combs, bigrams26)
comb_sum.sort(key=lambda comb: comb[1])

for comb in comb_sum:
    print(comb)
    print('hand switching frequency:', comb[1] / total_probability20, '\n')
