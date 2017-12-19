import numpy as np

BOUNDARY_CONDITIONS = {
    "top":    5,
    "right":  49,
    "bottom": 120,
    "left":   78
}

TEST_BOUNDARY_CONDITIONS = {
    "top":    100,
    "right":  50,
    "bottom": 0,
    "left":   75
}

TEST_EXPECTED_RESULT = np.array([
    [78.59, 76.06, 69.71],
    [63.21, 56.11, 52.34],
    [43.00, 33.30, 33.89]
])