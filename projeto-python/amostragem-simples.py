import pandas as pandas
import numpy as numpy

iris_register = pandas.read_csv('iris.csv')
tamanho_do_iris_register = iris_register.shape

numpy.random.seed(2345)
amostra_simples = numpy.random.choice(a=[0,1], size=150, replace=True, p=[0.5, 0.5])

tamanho_da_amostra = len(amostra_simples)
quantos_numeros_1 = len(amostra_simples[amostra_simples == 1])
quantos_numeros_0 = len(amostra_simples[amostra_simples == 0])
