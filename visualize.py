import numpy as np
import matplotlib.pyplot as plt


def plate(boundary_conditions):
    plt.xlim((-0.5, 4.5))
    plt.ylim((-0.5, 4.5))

    x = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
    y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])

    x1 = np.array([0, 1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0,
                   0, 0, 0, 0])

    y1 = np.array([0, 0, 0, 0, 0,
                   1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0])

    plt.plot(x1, y1)
    plt.scatter(x, y, s=50, color="red")

    plt.annotate(boundary_conditions["top"], xy=(2 - 0.1, 4 + 0.15))
    plt.annotate(boundary_conditions["bottom"], xy=(2 - 0.1, 0 - 0.25))
    plt.annotate(boundary_conditions["right"], xy=(4 + 0.1, 2 - 0.1))
    plt.annotate(boundary_conditions["left"], xy=(0 - 0.25, 2 - 0.1))

    plt.draw()


def difference_scheme():
    plt.xlim((-0.5, 4.5))
    plt.ylim((-0.5, 4.5))

    x = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
    y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])

    x2 = np.array([1, 2, 3])
    y2 = np.array([2, 2, 2])

    x3 = np.array([2, 2, 2])
    y3 = np.array([1, 2, 3])

    plt.plot(x3, y3, linestyle=":", color="red")
    plt.plot(x2, y2, linestyle=":", color="red")

    x1 = np.array([0, 1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0,
                   0, 0, 0, 0])

    y1 = np.array([0, 0, 0, 0, 0,
                   1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0])

    plt.plot(x1, y1)

    plt.scatter(x, y, s=50, color="red")

    plt.draw()


def marked_plate(annotations, boundary_conditions):
    plt.xlim((-0.5, 4.5))
    plt.ylim((-0.5, 4.5))

    x = np.array([1, 2, 3, 1, 2, 3, 1, 2, 3])
    y = np.array([1, 1, 1, 2, 2, 2, 3, 3, 3])

    x1 = np.array([0, 1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0,
                   0, 0, 0, 0])

    y1 = np.array([0, 0, 0, 0, 0,
                   1, 2, 3, 4,
                   4, 4, 4, 4,
                   3, 2, 1, 0])

    plt.plot(x1, y1)
    plt.scatter(x, y, s=50, color="red")

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            x = j + 1
            y = len(annotations) - i
            plt.annotate(annotations[i][j], xy=(x, y), xytext=(x - 0.24, y + 0.28))

    plt.annotate(boundary_conditions["top"], xy=(2 - 0.1, 4 + 0.15))
    plt.annotate(boundary_conditions["bottom"], xy=(2 - 0.1, 0 - 0.25))
    plt.annotate(boundary_conditions["right"], xy=(4 + 0.1, 2 - 0.1))
    plt.annotate(boundary_conditions["left"], xy=(0 - 0.25, 2 - 0.1))

    plt.draw()
