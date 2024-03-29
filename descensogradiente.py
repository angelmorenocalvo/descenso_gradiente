# -*- coding: utf-8 -*-
"""DescensoGradiente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oxq2Qz0LoCJ6rudwlfMJzb-uTxnIgnOF

Función que vamos a usar para el descenso del gradiente

$F(x,y) = sin(\frac{1}{2}x^2 - \frac{1}{4}y^2 + 3)cos(2x+1-e^y)$
"""

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

func = lambda th: np.sin(1/2 * th[0] ** 2 - 1/4 * th[1] ** 2 + 3) * np.cos(2 * th[0] + 1 - np.e**th[1])
# en funcion de (x,y) se escribiría como: np.sin(1/2) * x ** 2 -1/4* y**2 + 3)* np.cos(2*x +1 - np.e**y)
# donde th es el vector de parametros, que en ml suele ser la variable z(vector parametros)
res = 100 # Numero de cordenadas de lo ejes
_X = np.linspace(-2,2, res) # genera 100 valores desde -2 hasta 2
_Y = np.linspace(-2,2, res)

_Z = np.zeros((res,res)) # Matriz de 100 con tamaño res,res

for ix, x in enumerate(_X):
  for iy, y in enumerate(_Y):
    _Z[ix,iy] = func([x,y])

plt.contourf(_X,_Y,_Z, 100) # Con el 100 lo que conseguimos es poner el numero de anillas
# Si utilizamos contourf, nos da la funcion representada solida
# Pero sin la f salen las lineas de nivel
plt.colorbar()


Theta = np.random.rand(2)*4 -2

_T = np.copy(Theta)
h = 0.001 # diferencia entre el siguiende valor para calcular la diferencia, la cual sera la derivada
grad = np.zeros(2)
lr = 0.001# Learning rate
# Hacemos una aproximacion de las derivadas
plt.plot(Theta[0], Theta[1], "o", c = "white")
for _ in range(10000):
  for it, th in enumerate(Theta):
    _T = np.copy(Theta)
    
    _T[it] = _T[it] + h
    deriv = (func(_T)- func(Theta))/h
    grad[it] = deriv

  Theta = Theta - lr*grad
  #print(func(Theta))
  if(_%100 == 0):
    plt.plot(Theta[0], Theta[1], "o", c = "red")

plt.plot(Theta[0], Theta[1], "o", c = "green")
plt.show()

