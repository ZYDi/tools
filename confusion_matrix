from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


def plotCM(classes, matrix, savname):
    """classes: a list of class names"""
    # Normalize by row
    plt.switch_backend('agg')
    fig = plt.figure()
    ax = fig.add_subplot(111)
    cax = ax.matshow(matrix)
    fig.colorbar(cax)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, matrix[i, j], fontsize=15, va='center', ha='center')
    ax.set_xticklabels([''] + classes, rotation=0)
    ax.set_yticklabels([''] + classes)
    # save
    plt.savefig(savname)

if __name__ == '__main__':
    '''casme2
    classes = ['disgust', 'happiness', 'repression', 'surprise', 'sadneess']
    matrix = np.array([[0.84, 0.00, 0.08, 0.00, 0.08],
                       [0.00, 0.66, 0.17, 0.17, 0.00],
                       [0.20, 0.00, 0.60, 0.00, 0.20],
                       [0.00, 0.20, 0.00, 0.80, 0.00],
                       [0.50, 0.00, 0.00, 0.00, 0.50]])
    '''
    '''samm
    classes = ['anger', 'contempt', 'happiness', 'surprise']
    matrix = np.array([[0.73, 0.18, 0.09, 0.00],
                       [0.50, 0.50, 0.00, 0.00],
                       [0.00, 0.20, 0.60, 0.20],
                       [0.00, 0.00, 0.00, 1.00]])
    '''

    '''smic'''
    classes = ['positive', 'negative', 'surprise']
    matrix = np.array([[0.70, 0.10, 0.20],
                       [0.14, 0.72, 0.14],
                       [0.11, 0.11, 0.78]])

    plotCM(classes, matrix, "cm_smic.png")
