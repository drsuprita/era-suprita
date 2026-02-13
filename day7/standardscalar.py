import math
import numpy as np
def std_scalar(data):

    mean=sum(data) / len(data)
    variance=sum((x - mean) ** 2 for x in data) / len(data)
    sd=math.sqrt(variance)
    return [(x - mean) / (sd) for x in data]

numbers = [2, 4, 6, 8, 10]

print("standardscalar:",std_scalar(numbers))