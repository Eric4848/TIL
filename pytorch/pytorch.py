import torch
import numpy as np

a = torch.ones(7)
b = a.numpy()
a.add_(1)
print(a)
print(b)

a = np.ones(7)
b = torch.from_numpy(a)
np.add(a, 1, out=a)
print(a)
print(b)