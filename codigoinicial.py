#Inicindo o Projeto


#Importando bibliotecas:
from re import L
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *


#Indicando constantes iniciais:


#Lc = 46 e L são a msm coisa????
cc = 1.59 #
cp = 2.0
ec = 0.001 #espessura do chocolate 
ep = 0.005
Vc = 0.027 #volume do chocolate 
mc = 0.2 #massa chocolate
mp = 0.5
p = mc/ Vc #
kc = 0.163 #koeficiente de condutividade do chocolate
kp = 13.8
A = 0.09 #Area, a mesma para os dois pois significa a area de contato do chocolate com a panela
har =  0.03 #
L = 0.31 #




#Implementando a função

def modelo(x,t): # Ta retornando os Qs como lista e eu quero que seja apenas um valor 
    # Indicando primeiros parametros: 
    Tp = x[0]
    Tc = x[1] 
    Q1 = (Tp - 100)/((ep / 2)/(kp*A))
    Q2 = (Tp - Tc)/((ep/2)/(kp*A)) + ((ec/2)/(kc*A))
    Q3 = (Tc-25)/((ec/2)/(kc*A)) + (1/(har*A))

    dTpdt = (Q1 - Q2) / (mp*cp)
    for i in Tc:
        if Tc <= 25:
            dTcdt =(Q2-Q3)/(mc*cc)
        else:
            dTcdt = (Q2-Q3)/L #dMsdt
    dxdt = [dTpdt,dTcdt]
    return dxdt


#Condições iniciais 
Tp0 = 25 #vai começar com a temperatura ambiente ???
Tc0 = 25

X0 = [Tp0,Tc0]

dt = 60 #segundos 

t_lista = np.arange(0,100,dt)

y = odeint(modelo,X0, t_lista)

Tp = y[:,0]
Tc = y[:,1]

# Plota resultados
plt.plot(t,Tp,label='Temperatura da panela')
plt.plot(t,Tc,label='Temperatura do chocolate')
plt.xlabel('Tempo ($min$)')
plt.ylabel('Temperatura ($^{\circ}C$)')
plt.legend()
plt.grid()
plt.show()

    

