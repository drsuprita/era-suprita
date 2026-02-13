import math
import numpy as np
numbers = [2, 4, 6, 8, 10]
sigmoid = [1 / (1 + math.exp(-x)) for x in numbers]
print("Sigmoid values:", sigmoid)