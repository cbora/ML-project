import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn import random_projection

def pca_project(A, n_components=1):
    X_proj = PCA(n_components=n_components).fit_transform(A)
    X_proj = X_proj/np.linalg.norm(X_proj)
    return X_proj


def cca_project(A, d):
    M = np.dot(A.T, A)
    print M.shape
    w, v = np.linalg.eigh(
        np.linalg.inv(M[d/2:, d/2:])
        * M[d/2:, :d/2]
        * np.linalg.inv(M[:d/2, :d/2])
        * M[:d/2,d/2:])

    X1 = np.copy(A[:, :d/2])
    W1 = np.copy(v[:, 0])
    
    Y1 = np.dot(A[:, :d/2], v[:, 0])

    w2, v2 = np.linalg.eigh(
        np.linalg.inv(M[d/2:, d/2:])
        * M[d/2:,:d/2]
        * np.linalg.inv(M[:d/2,:d/2])
        * M[:d/2,d/2:])
    
    Y2 = np.dot(A[:, d/2:], v2[:, 0])

    return (Y1, Y2)

def randomprojection_project(XX, n_components=1):
    Y_proj = random_projection.GaussianRandomProjection(n_components=n_components).fit_transform(XX)
    return Y_proj

def kmeans(X, K=2, centers=None, verbose=0):
    if centers:
        k_means = KMeans(n_clusters=K, verbose=verbose, init=centers, n_init=1)
    else:
        k_means = KMeans(n_clusters=K, verbose=verbose)
    k_means.fit(X)
    y_pred = k_means.predict(X)
    return (y_pred, k_means.cluster_centers_, k_means.labels_)

def singlelink(X, K):
    Z = linkage(X)
    clusters = fcluster(Z, K, criterion='maxclust')
    #clusters -=
    return (clusters, Z)
