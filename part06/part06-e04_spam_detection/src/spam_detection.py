#!/usr/bin/env python3

import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

def spam_detection(random_state=0, fraction=1.0):
    model = MultinomialNB()
    cv = CountVectorizer()

    with gzip.open('src/spam.txt.gz', 'rb') as f: # Opening file
        spam = f.readlines()
        length = int(len(spam) * fraction)
        spam = spam[:length]
    with gzip.open('src/ham.txt.gz', 'rb') as f: # Opening file
        ham = f.readlines()
        length = int(len(ham) * fraction)
        ham = ham[:length]

    arr = np.concatenate( (ham, spam) )
    feature = cv.fit_transform(arr).toarray()
    label = np.concatenate( (np.zeros(len(ham)), np.ones(len(spam))) )

    X_train, X_test, y_train, y_test = train_test_split( feature, label, test_size=0.25, random_state=random_state )
    model.fit(X_train, y_train)
    y_fitted = model.predict(X_test)

    n = len(y_test) # Amount of all test cases
    acc = metrics.accuracy_score(y_test, y_fitted)
    return acc, n, n - int(n * acc) # accuracy, all cases, failed cases

def main():
    accuracy, total, misclassified = spam_detection(0, 0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
