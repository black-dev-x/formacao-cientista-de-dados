import numpy as numpy
import pandas as pandas

from math import ceil

populacao = 150
amostra = 15

divisor = ceil(populacao/amostra)

randomStarter = numpy.random.randint(low = 1, high = divisor + 1, size = 1)[0]

sorteados = []

for i in range(amostra):
    sorteados.append(randomStarter + (i*divisor))
    
iris = pandas.read_csv('iris.csv')

amostra_iris = iris.loc[sorteados]