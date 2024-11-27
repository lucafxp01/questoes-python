"""
Use numpy.linspace para criar um array com 50 valores igualmente
espaçados entre 0 e 10. Use numpy.arange para criar um array com
valores de 0 a 10, incrementando de 0.2
"""
import numpy as np

lins = np.linspace(0, 10, 50)
print(lins)

array = np.arange(0, 10.2, 0.2)
print(array)