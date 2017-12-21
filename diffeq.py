import numpy as np
from config import TEST_BOUNDARY_CONDITIONS, TEST_EXPECTED_RESULT


class BoundaryProblem:
    """
        Solving boundary problem for Laplace's equation
    """

    def __init__(self, boundary_conditions, change_interval, amount_of_sections):
        """
        :param boundary_conditions: dict with boundary problem initial state
        :param change_interval: set the axis change interval
        :param amount_of_sections: tuple with number of segments of a partition by each axis 
        """

        self._boundary_conditions = boundary_conditions
        self._change_interval = change_interval
        self._amount_of_sections = amount_of_sections

    def solve(self, method="grid", disp=False):
        result = None

        if method == "grid":
            result = self._grid_method(disp)

        return result

    def _grid_method(self, disp):
        """
        Method that solve boundary problem using grid method
        
        :param disp: boolean that dtermines whether to display details of calculations on the screen
        :return: numpy array with grip result
        """

        N, M = self._amount_of_sections
        x_interval, y_interval = self._change_interval

        A = np.zeros((N * M, N * M))
        b = np.zeros((N * M, 1))

        h1 = x_interval / N
        h2 = y_interval / M

        for i in range(N):
            for j in range(M):
                if j == 0:
                    A[j + i * N][i + M * j] = 1
                    b[j + i * N] = self._boundary_conditions["left"]
                    continue
                if j == M - 1:
                    A[j + i * N][i + M * j] = 1
                    b[j + i * N] = self._boundary_conditions["right"]
                    continue
                if i == 0:
                    A[j + i * N][i + M * j] = 1
                    b[j + i * N] = self._boundary_conditions["bottom"]
                    continue
                if i == N - 1:
                    A[j + i * N][i + M * j] = 1
                    b[j + i * N] = self._boundary_conditions["top"]
                    continue

                A[j + i * N][i + M * j] = -2 / (h1 ** 2) - 2 / (h2 ** 2)
                A[j + i * N][i + M * (j - 1)] = 1 / (h2 ** 2)
                A[j + i * N][i + M * (j + 1)] = 1 / (h2 ** 2)
                A[j + i * N][(i - 1) + M * j] = 1 / (h1 ** 2)
                A[j + i * N][(i + 1) + M * j] = 1 / (h1 ** 2)

        raw_res = np.linalg.solve(A, b)

        result = np.empty((N - 2, M - 2))

        for i in range(N - 2):
            for j in range(M - 2):
                result[(N - 2) - 1 - i][j] = np.around(raw_res[(i + 1) + M * (j + 1)][0], 2)

        if disp:
            print("Input data\n"
                  "\tTemperature on\n"
                  "\t\tupper edge: {}\n"
                  "\t\tright edge: {}\n"
                  "\t\tlower edge: {}\n"
                  "\t\tleft edge: {}\n"
                  "Computational data\n"
                  "\tStep size\n"
                  "\t\tby X axis: {}\n"
                  "\t\tby Y axis: {}\n"
                  "\tAmount of equations: {}\n".format(self._boundary_conditions["top"],
                                                       self._boundary_conditions["right"],
                                                       self._boundary_conditions["bottom"],
                                                       self._boundary_conditions["left"],
                                                       h1, h2, len(A) - 4))

        return result

    @staticmethod
    def is_valid(disp=False):
        """
        Method that compare expected test result and actual test result.
        
        :return: boolean
        """
        equals = True
        expected = TEST_EXPECTED_RESULT

        if disp:
            print("RUN METHOD WITH TEST DATA\n")

        result = BoundaryProblem(boundary_conditions=TEST_BOUNDARY_CONDITIONS,
                                 change_interval=(5, 5),
                                 amount_of_sections=(5, 5)).solve(method="grid", disp=disp)

        for i in range(len(result)):
            for j in range(len(result[i])):
                if abs(result[i][j] - expected[i][j]) > 0.5:
                    equals = False
        if disp:
            print("EXPECTED RESULT")
            print(expected)
            print("ACTUAL RESULT")
            print(result)
            print("\n")

        return equals
