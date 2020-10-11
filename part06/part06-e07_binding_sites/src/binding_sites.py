#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

# A -> 0
# C -> 1
# G -> 2
# T -> 3
def toint(c):
    if c == 'A': return 0
    elif c == 'C': return 1
    elif c == 'G': return 2
    else: return 3 # c = T
    
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    X = np.array(df.iloc[:, 0]) #Feature
    X = [ [toint(c) for c in s] for s in X ]
    y = df.iloc[:, 1] #label
    return (np.array(X), y)

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    X, y = get_features_and_labels(filename)
    model = AgglomerativeClustering(linkage='average', affinity='euclidean').fit(X)

    permutation = find_permutation(len(set(y)), y, model.labels_) # len(set(y)): cluster count
    new_labels = [ permutation[label] for label in model.labels_]   # permute the labels

    return accuracy_score(y, new_labels)

def cluster_hamming(filename):
    X, y = get_features_and_labels(filename)
    X = pairwise_distances(X, metric='hamming')
    model = AgglomerativeClustering(linkage='average', affinity='precomputed').fit(X)

    permutation = find_permutation(len(set(y)), y, model.labels_) # len(set(y)): cluster count
    new_labels = [ permutation[label] for label in model.labels_]   # permute the labels
    return accuracy_score(y, new_labels)


def main():
    # print(toint(["GGATAATA","CGATAACC"])) # test toint
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))

if __name__ == "__main__":
    main()
