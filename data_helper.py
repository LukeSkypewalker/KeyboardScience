from collections import namedtuple

Bigram = namedtuple("Bigram", ['first', 'second', 'frequency'])


def get_data(file_location):
    input_data_file = open(file_location, 'r')
    input_data = ''.join(input_data_file.readlines())
    input_data_file.close()
    return input_data


def get_bigrams_list(input_data):
    bigrams = []
    lines = input_data.split('\n')
    for line in lines:
        a = line[0]
        b = line[1]
        frequency = int(line[3:])
        bigrams.append([a, b, frequency])
    return bigrams


def get_bigrams_dict(input_data):
    bi_dict = {}
    lines = input_data.split('\n')
    for line in lines:
        a = line[0]
        b = line[1]
        frequency = int(line[3:])
        bi_dict[a, b] = frequency
    return bi_dict


def get_freq_dict(input_data):
    f_dict = {}
    lines = input_data.split('\n')
    for line in lines:
        letter = line[0]
        frequency = float(line[2:])
        f_dict[letter] = frequency
    return f_dict


# def store_to_file(comb_sum, filename):
#     target = open(filename, 'w')
#     target.truncate()
#     target.write('\n'.join('%s ' % x for x in comb_sum))
#     target.close()
#     return


def store_to_file(data, filename):
    with open(filename, 'w') as file:
        file.write('\n'.join('%s ' % x for x in data))
    return


if __name__ == '__main__':

    bigrams = get_bigrams_list(get_data('data/bigrams26.txt'))
    from pprint import pprint
    pprint(bigrams)

    # pprint(get_freq_dict(get_data('data/freq_norvig.txt')))

