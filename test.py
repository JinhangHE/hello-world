import numpy as np

data = np.random.randn(2,3)



data = np.zeros((3,6))

data = np.arange(15)

data = data.astype(np.float64)

data = np.array([[1,3,2],[2,-9.6,'a']], dtype=np.unicode_)

print(data)

print(data.shape)

print(data.dtype)

print(data.ndim)
