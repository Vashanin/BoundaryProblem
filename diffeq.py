import numpy as np
from config import BOUNDARY_CONDITIONS, TEST_BOUNDARY_CONDITIONS, TEST_EXPECTED_RESULT
from test import SolverValidation


class BoundaryProblem:
    """
        Solving boundary problem for Laplace's equation
    """
    def __init__(self, boundary_conditions):
        self._boundary_conditions = boundary_conditions

    def solve(self, method="grid"):
        result = None

        if method == "grid":
            result = self._grid_method()

        return result

    def _grid_method(self):
        N = 5
        M = 5
        X_RANGE = 5
        Y_RANGE = 5

        A = np.zeros((N * M, N * M))
        b = np.zeros((N * M, 1))

        h1 = X_RANGE / N
        h2 = Y_RANGE / M

        # CHECK THE INDEXING!!!

        for i in range(N):
            for j in range(M):
                if j == 0:
                    A[j + i * 5][i + 5 * j] = 1
                    b[j + i * 5] = self._boundary_conditions["left"]
                    continue
                if j == 4:
                    A[j + i * 5][i + 5 * j] = 1
                    b[j + i * 5] = self._boundary_conditions["right"]
                    continue
                if i == 0:
                    A[j + i * 5][i + 5 * j] = 1
                    b[j + i * 5] = self._boundary_conditions["bottom"]
                    continue
                if i == 4:
                    A[j + i * 5][i + 5 * j] = 1
                    b[j + i * 5] = self._boundary_conditions["top"]
                    continue

                A[j + i * 5][i + 5 * j] = -2 / (h1 ** 2) - 2 / (h2 ** 2)
                A[j + i * 5][i + 5 * (j - 1)] = 1 / (h2 ** 2)
                A[j + i * 5][i + 5 * (j + 1)] = 1 / (h2 ** 2)
                A[j + i * 5][(i - 1) + 5 * j] = 1 / (h1 ** 2)
                A[j + i * 5][(i + 1) + 5 * j] = 1 / (h1 ** 2)

        raw_res = np.linalg.solve(A, b)

        # FIX THE CRUTCH HERE!!!
        # result = np.zeros(((N - 2) * (M - 2)))
        result = np.array([
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ])

        for i in range(N - 2):
            for j in range(M - 2):
                result[i][j] = raw_res[(i + 1) + 5 * (j + 1)][0]

        return result


boundary_problem = BoundaryProblem(boundary_conditions=BOUNDARY_CONDITIONS).solve(method="grid")
print("Answer: ")
print(boundary_problem)

test_result = BoundaryProblem(boundary_conditions=TEST_BOUNDARY_CONDITIONS).solve(method="grid")
test_expected_result = TEST_EXPECTED_RESULT

print("\nIs tests converge: " + str(SolverValidation.compare(test_result, test_expected_result)))