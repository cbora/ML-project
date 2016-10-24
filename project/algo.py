import numpy as np
import math
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn import random_projection
from sklearn.cluster import spectral_clustering
#import sklearn.mixture
from sklearn.mixture.gmm import GMM
from sklearn.manifold import SpectralEmbedding
from sklearn.decomposition import LatentDirichletAllocation as LDAalgo

def pca_project(A, n_components=1):
    """
    PCA 

    returns vector
    """
    X_proj = PCA(n_components=n_components).fit_transform(A)
    X_proj = X_proj/np.linalg.norm(X_proj)
    return X_proj


def cca_project(A, d):
    """ CCA 
    returns tuple of Y1 and Y2
    """
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
    """ Random projection. 

    returns a tuple of Clusters and cluster centers
    """
    Y_proj = random_projection.GaussianRandomProjection(n_components=n_components).fit_transform(XX)
    return Y_proj

def kmeans(X, K=2, centers=None, verbose=0):
    if centers is not None:
        k_means = KMeans(n_clusters=K, verbose=verbose, init=centers, n_init=1)
    else:
        k_means = KMeans(n_clusters=K, verbose=verbose)
    k_means.fit(X)
    y_pred = k_means.predict(X)
    return (y_pred, k_means.cluster_centers_)

def singlelink(X, K):
    """ Single link algorithm
    returns a tuple containing clusters and Z
    """
    Z = linkage(X)
    clusters = fcluster(Z, K, criterion='maxclust')
    #clusters -=
    return (clusters, Z)

def spectral(graph, n_clusters=10, solver='arpack'):
    labels =spectral_clustering(graph, n_clusters=n_clusters, eigen_solver=solver)
    return labels

def gmm(X, n_components=10, centers=None):
    g = GMM(n_components=n_components, covariance_type='full', n_iter=10000).fit(X)
    print g.converged_
    #, means_init=centers).fit(X
    labels = g.predict(X)
    return labels

def embedding(graph, n_components=10):
    Y = SpectralEmbedding(n_components=n_components).fit_transform(graph)
    return Y
