"""
Crie uma matriz 2x2 para representar uma transformação linear e um vetor
v=[1,2]. Aplique a transformação ao vetor v multiplicando-o pela matriz.

"""

import numpy as np


M = np.array([[2, 1],
              [0, 3]])

v = np.array([1, 2])

resultado = np.dot(M, v)

print(resultado)
