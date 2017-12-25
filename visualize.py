import numpy as np
import matplotlib.pyplot as plt


def plate(boundary_conditions, amount_of_sections, options=None):
    N, M = amount_of_sections

    plt.xlim((-0.75, M + 0.75))
    plt.ylim((-0.75, N + 0.75))

    x = []
    for i in range(1, M):
        x.append(i)
    x *= (N - 1)

    y = []
    for i in range(1, N):
        y += ([i] * (M - 1))

    x = np.array(x)
    y = np.array(y)

    x1 = np.array([0, M, M, 0, 0])
    y1 = np.array([0, 0, N, N, 0])

    plt.plot(x1, y1)
    plt.scatter(x, y, s=50, color="red")

    plt.annotate(boundary_conditions["top"], xy=(M/2 + 0.5, N + 0.15))
    plt.annotate(boundary_conditions["bottom"], xy=(M/2 + 0.5, 0 - 0.5))
    plt.annotate(boundary_conditions["right"], xy=(M + 0.1, N/2 - 0.1))
    plt.annotate(boundary_conditions["left"], xy=(0 - 0.5, N/2 - 0.1))

    if options is not None:
        if options["show_coord"]:
            for x in range(1, M):
                for y in range(1, N):
                    plt.annotate("({};{})".format(x, y), xy=(x - 0.2, y + 0.2))
        if options["show_grid"]:
            plt.grid()

    plt.draw()


def difference_scheme(amount_of_sections):
    N, M = amount_of_sections

    plt.xlim((-0.75, M + 0.75))
    plt.ylim((-0.75, N + 0.75))

    x = []
    for i in range(1, M):
        x.append(i)
    x *= (N - 1)

    y = []
    for i in range(1, N):
        y += ([i] * (M - 1))

    x = np.array(x)
    y = np.array(y)

    x1 = np.array([0, M, M, 0, 0])
    y1 = np.array([0, 0, N, N, 0])

    plt.plot(x1, y1)

    x2 = np.array([1, 2, 3])
    y2 = np.array([2, 2, 2])

    x3 = np.array([2, 2, 2])
    y3 = np.array([1, 2, 3])

    plt.plot(x3, y3, linestyle=":", color="red")
    plt.plot(x2, y2, linestyle=":", color="red")

    plt.grid()

    plt.scatter(x, y, s=50, color="red")

    plt.draw()


def marked_plate(annotations, amount_of_sections, boundary_conditions):
    N, M = amount_of_sections

    plt.xlim((-0.75, M + 0.75))
    plt.ylim((-0.75, N + 0.75))

    x = []
    for i in range(1, M):
        x.append(i)
    x *= (N - 1)

    y = []
    for i in range(1, N):
        y += ([i] * (M - 1))

    x = np.array(x)
    y = np.array(y)

    x1 = np.array([0, M, M, 0, 0])
    y1 = np.array([0, 0, N, N, 0])

    plt.plot(x1, y1)
    plt.scatter(x, y, s=50, color="red")

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            x = j + 1
            y = len(annotations) - i
            plt.annotate(annotations[i][j], xy=(x, y), xytext=(x - 0.24, y + 0.28))

    plt.annotate(boundary_conditions["top"], xy=(M / 2 + 0.5, N + 0.15))
    plt.annotate(boundary_conditions["bottom"], xy=(M / 2 + 0.5, 0 - 0.5))
    plt.annotate(boundary_conditions["right"], xy=(M + 0.1, N / 2 - 0.1))
    plt.annotate(boundary_conditions["left"], xy=(0 - 0.5, N / 2 - 0.1))

    plt.draw()
