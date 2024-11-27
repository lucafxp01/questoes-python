"""
Crie uma matriz 4x4 preenchida com números de 1 a 16. Obtenha a
transposta dessa matriz e multiplique a matriz original pela transposta.
"""
import numpy as np


matriz = np.arange(1, 17).reshape(4, 4)
print("Matriz original:")
print(matriz)

matriz2 = np.transpose(matriz)
print("\nMatriz transposta:")
print(matriz2)

resultado = np.dot(matriz, matriz2)
print("\nResultado da multiplicação:")
print(resultado)

