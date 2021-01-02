from itertools import permutations

from hand_calc_flow import calc_flow
from data import *

# left_hand_layout_combs = combinations(letters8, len(letters8) // 2)
# comb_sums = calc_combs_sums(left_hand_layout_combs, bigrams8)

layouts = list(permutations(letters8))
# print(*left_hand_layout_combs, sep='\n')
scores = [(layout, calc_flow(layout, bigrams8)) for layout in layouts]

scores.sort(key=lambda comb: comb[1])
data = [(x, x[1]/total_probability8) for x in scores]
print(*data, sep='\n')


