import random
import numpy

# Probabilidade de tirar uma flor no truco

count = 0 # Contador de flor

for i in range(1, 1000001):
    n = numpy.array(random.sample(range(1, 41), 3)) # Escolhendo 3 números não repetidos de 1 a 40 e colocando em um vetor
    n1 = (n <= 10).all() # flor de um naipe quando n[0], n[1], n[2] <= 0
    if n1:
        count = count + 1

prob = (count * 4) / i # Multiplicar por 4 pois são 4 naipes

print(prob) # ~ 0.04898

# Faz sentido pois, (40/40) * (9/39) * (8/38) ~= 0.04858
