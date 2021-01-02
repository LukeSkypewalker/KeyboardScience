from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np

from trash.data_letters_processor import get_bigram_list_summarized
from data import *

# data = get_bigram_list_summarized('E', bigrams)
# data = [get_bigram_list_summarized(letter) for letter in letters26]
data_list = [get_bigram_list_summarized(letter, bigrams26) for letter
             in ['X', 'J', 'Q', 'Z']]
data = [val for sublist in data_list for val in sublist]

pprint(data)


y_letters = ([data[i][0] for i in range(len(data))])
y = list(range(len(data)))
# y.reverse()
freaquency = ([data[i][1] for i in range(len(data))])
freq0 = ([data[i][2][:][0][2] for i in range(len(data))])
freq1 = ([data[i][2][:][1][2] for i in range(len(data))])
print(freaquency)
print(freq0)
print(freq1)
print(y_letters)
print(y)

plt.rcdefaults()
width = 1  # the width of the bars: can also be len(x) sequence
p1 = plt.bar(y, freq0, width, color='r')
p2 = plt.bar(y, freq1, width, color='y', bottom=freq0)
plt.ylabel('Scores')
plt.title('Scores')
y = np.array(y)
plt.xticks(y+width/2., y_letters)
plt.show()
