import numpy as np

scores = np.random.randint(50, 101, size=(5, 3))
means = scores.mean(axis=0)
centered_scores = scores - means

print(scores)
print(centered_scores)
