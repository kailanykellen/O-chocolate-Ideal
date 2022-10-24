#Inicindo o Projeto
#testando o git


#Importando bibliotecas:
from re import L
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from math import *


#Indicando constantes iniciais:


#Lc = 46 e L são a msm coisa????
cc = 1.59 #calor especifico chocolate
cp = 0.22
A = 0.005 #Area, a mesma para os dois pois significa a area de contato do chocolate com a panela
ec = 0.02 #espessura do chocolate 
ep = 0.01
Vc = A* ec #volume do chocolate 
mc = 0.09 #massa chocolate
mp = 0.1
rho = mc/ Vc #densidade do chocolate
kc = 0.163 #koeficiente de condutividade do chocolate
kp = 238
har =  0.03 #coeficiente de convecção do ar 
L = 46*1000 #Calor latente do chocolate




#Implementando a função

def modelo(x,t): # Ta retornando os Qs como lista e eu quero que seja apenas um valor 
    # Indicando primeiros parametros: 
    Tp = x[0]
    Tc = x[1] 
    M = x[2]
    Q1 = (100 - Tp)/((ep / 2)/(kp*A))
    Q2 = (Tp - Tc)/(((ep/2)/(kp*A)) + ((ec/2)/(kc*A)))
    Q3 = (25 - Tc)/(((ec/2)/(kc*A)) + (1/(har*A)))

    dTpdt = (Q1 - Q2) / (mp*cp)
    dTcdt = (Q2-Q3)/(mc*cc)
    
    if Tc < 36:
        dMdt = 0        
    else:
        dMdt = -(Q2-Q3)/L #dMsdt
        dTcdt = 0 
    dxdt = [dTpdt,dTcdt,dMdt]
    return dxdt


#Condições iniciais 
Tp0 = 25 #vai começar com a temperatura ambiente ???
Tc0 = 25
M0 = mc

X0 = [Tp0,Tc0, M0]

dt = 1e-3 #min

t_lista = np.arange(0,15,dt)

y = odeint(modelo,X0, t_lista)

Tp = y[:,0]
Tc = y[:,1]
M = y[:,2]

# Plota resultados
plt.plot(t_lista,Tp,'black',label='Temperatura da panela')
plt.plot(t_lista,Tc,label='Temperatura do chocolate')
plt.xlabel('Tempo ($min$)')
plt.ylabel('Temperatura ($^{\circ}C$)')
plt.legend()
plt.grid()
plt.show()

plt.plot(t_lista,M,label='Massa do chocolate')
plt.xlabel('Tempo ($min$)')
plt.ylabel('Massa (Kg)')
plt.legend()
plt.grid()
plt.show()