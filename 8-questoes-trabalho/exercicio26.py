"""
Crie um array com 30 números inteiros aleatórios entre 0 e 10. Identifique os
valores únicos e conte a frequência de cada valor
"""
import numpy as np  

array = np.random.randint(0, 11, size=30)  
unico = np.unique(array)  

frequencia = {}  
for num in array:  
    num_int = int(num)    
    if num_int in frequencia:  
        frequencia[num_int] += 1  
    else:  
        frequencia[num_int] = 1  

print(array)  
print(unico)  
print(frequencia)  