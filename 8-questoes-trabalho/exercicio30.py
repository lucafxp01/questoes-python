"""
Crie um conjunto de dados simulando uma relação linear: y=2x+3+ruído,
onde x varia de 0 a 10 (20 pontos). Use a álgebra matricial do NumPy para
calcular os coeficientes da regressão linear y=ax+b. Compare os resultados
com os obtidos usando a função numpy.polyfit
"""

import numpy as np


np.random.seed(42) 
x = np.linspace(0, 10, 20)
ruido = np.random.normal(0, 1, x.shape)
y = 2 * x + 3 + ruido


X = np.vstack([x, np.ones(len(x))]).T
A, B = np.linalg.lstsq(X, y, rcond=None)[0]


coef_polyfit = np.polyfit(x, y, 1)

print(f"Coeficientes usando álgebra matricial: a = {A}, b = {B}")
print(f"Coeficientes usando numpy.polyfit: a = {coef_polyfit[0]}, b = {coef_polyfit[1]}")
