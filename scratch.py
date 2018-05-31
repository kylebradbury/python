# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

np.random.seed(42)
all_words  = pd.read_table('./data/wordlist.txt', header=None)
word_array = all_words.values.flatten()
word_array.shape
list1      = np.random.choice(word_array, size=(5000,), replace=False)
list2      = np.random.choice(word_array, size=(5000,), replace=False)

ncommon = 0
common_words = []
for word in list1:
    if word in list2:
        ncommon += 1
        common_words.append(word)

