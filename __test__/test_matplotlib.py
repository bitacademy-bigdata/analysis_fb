import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn


def ex1():
    # plt.plot([1, 2, 3, 4], [10, 20, 30, 40])
    plt.plot([10, 20, 30, 40])
    plt.show()


def ex2():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 1, 1)
    sp1.plot([1, 2, 3, 4], [10, 20, 30, 40])

    sp2 = fig.add_subplot(2, 1, 2)
    sp2.plot([1, 2, 3, 4], [100, 200, 300, 400])

    plt.show()


def ex3():
    fig = plt.figure()

    sp1 = fig.add_subplot(2, 2, 1)
    sp1.plot(randn(50).cumsum(), 'k--')

    sp2 = fig.add_subplot(2, 2, 2)
    sp2.hist(randn(1000), bins=20, color='k', alpha=0.3)

    sp3 = fig.add_subplot(2, 2, 3)
    sp3.scatter(np.arange(100), np.arange(100) + 3 * randn(100))


    plt.show()


def ex4():
    fig, subplot = plt.subplots(1, 1)
    subplot.plot([10, 20, 30, 40])
    plt.show()


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()
    # ex4()
