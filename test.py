class SolverValidation:
    @staticmethod
    def compare(result, expected):
        equals = True

        for i in range(len(result)):
            for j in range(len(result[i])):
                if abs(result[i][j] - expected[i][j]) > 1e-2:
                    equals = False

        print("\nActual answer")
        print(result)
        print("Expected result")
        print(expected)

        return equals
