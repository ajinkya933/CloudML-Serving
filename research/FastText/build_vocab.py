import pandas as pd

from utils.commons import FEATURE_COL, PAD_WORD

__author__ = 'KKishore'


def build_vocab(file_name):
    data_set = pd.read_csv(file_name)
    sentences = data_set[FEATURE_COL].values
    vocab_set = set()
    for sentence in sentences:
        text = str(sentence)
        words = text.split(' ')
        word_set = set(words)
        vocab_set.update(word_set)
    # vocab_set.remove('')
    return list(vocab_set)


vocab_list = build_vocab('dataset/trainpreprocess.csv')

with open('dataset/vocab.csv', 'w', encoding='utf-8') as vocab_file:
    vocab_file.write("{}\n".format(PAD_WORD))
    for word in vocab_list:
        vocab_file.write("{}\n".format(word))

with open('dataset/nwords.csv', mode='w') as n_words:
    n_words.write(str(len(vocab_list)))
