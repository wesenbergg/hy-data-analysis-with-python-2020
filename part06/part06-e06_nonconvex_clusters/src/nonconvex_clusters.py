#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df = pd.DataFrame(columns=['eps', 'Score', 'Clusters', 'Outliers'])
    df_data = pd.read_csv('src/data.tsv', sep='\t')
    X = df_data.iloc[:, 0:2]
    y = df_data.iloc[:, 2]
    original_cluster_count = len(set(y)) # Clusters
    cluster_count = 0
    # plt.scatter(df_data.iloc[:, 0], df_data.iloc[:, 1]) #data visualization
    
    for eps in np.arange(0.05, 0.2, 0.05):
        model = DBSCAN(eps=eps)
        model.fit(X)
        
        cluster_count = len(set(model.labels_)) # Clusters
        outliers = list(model.labels_).count(-1) # Outliers
        if -1 in model.labels_:
            cluster_count -= 1
        
        if original_cluster_count != cluster_count:
            acc = np.nan
        else:
            m = model.labels_ != -1
            permutation = find_permutation(cluster_count, y, model.labels_)
            new_labels = np.array([ permutation[label] for label in model.labels_])  # permute the labels
            acc = accuracy_score(y[m], new_labels[m])
        
        df = df.append({'eps': eps, 'Score': acc, 'Clusters': cluster_count, 'Outliers': outliers}, ignore_index=True)
    return df

def main():
    print(nonconvex_clusters())
    # plt.show()

if __name__ == "__main__":
    main()
