"""
5.Crie uma matriz 3x3 com números aleatórios entre 1 e 9. Redimensione-a
para 1x9 (flatten) e, em seguida, transforme-a em uma matriz 9x1.

"""
import numpy as np

matriz = np.random.randint(1, 10, (3,3))
print(matriz)
matriz2 = matriz.flatten()
print("\nmatriz flatten:") 
print(matriz2)

matriz3 = matriz2.reshape(9,1)
print("\nmatriz 9x1:") 
print(matriz3)