#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return list(lines)

def get_features(a):
    cv = CountVectorizer(token_pattern='(?u)\\w|-', analyzer='char', vocabulary=alphabet_set)
    arr = cv.fit_transform(a).toarray() #From first column to last
    return np.roll(arr, -1, axis=1)

def contains_valid_chars(s):
    for c in s.lower():
        if c not in alphabet_set:
            return False
    return True

def get_features_and_labels():
    fi_words = load_finnish() #np.char.lower(load_finnish())
    en_words = list( filter( lambda x: x[0].islower(), load_english() ))

    fi_words = list(filter(lambda x: contains_valid_chars(x), fi_words))
    en_words = list(filter(lambda x: contains_valid_chars(x), en_words))

    feature = np.concatenate( (get_features(fi_words), get_features(en_words)) )
    label = np.concatenate( (np.zeros(len(fi_words)), np.ones(len(en_words))) )
    return feature, label


def word_classification():
    feature, label = get_features_and_labels()
    cross_val = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    return cross_val_score(MultinomialNB(), X=feature, y=label, cv=cross_val)


def main():
    # L = ["-Achilles", "Achilles's", "Aconcagua", "Aconcagua's", "Acosta", "Acosta's", "Acropolis", "Acrux", "Acrux's", "Actaeon", "Actaeon's"]
    # print(get_features(L)) # PART 1
    # for s in L:
    #     print(contains_valid_chars(s)) # PART 2
    # f, t = get_features_and_labels() # PART 3
    # print(len(f))
    print("Accuracy scores are:", word_classification()) # PART 4

if __name__ == "__main__":
    main()
