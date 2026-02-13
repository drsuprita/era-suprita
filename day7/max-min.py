import math
import numpy as np
def min_max(data):
    xi=max(data)
    xj=min(data)
    return [(x - xj) / (xi - xj) for x in data]

numbers = [2, 4, 6, 8, 10]

print("Min-max:",min_max(numbers))