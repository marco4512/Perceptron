from ast import While
from cmath import exp
from decimal import Decimal
import  random
import math
from this import d
from warnings import catch_warnings
import numpy as np
import pandas as pd
from pyrfc3339 import generate
from tabulate import tabulate
cadena=""
x_0=[]
x_1=[]
x_2=[]
x_Correctos=[]
aux=True
listaPesos=[]
listaErrores=[]
listaY2=[]
alfa=0.4
def Modificacion_1 (cant,aux,operacion,x_Correctos):
    x_0.append('1')
    x_0.append('1')
    x_0.append('1')
    x_0.append('1')
    for can in range(int(cant/2)):
        x_1.append('1')
    for can in range(int(cant/2)):
        x_1.append('-1')
    for can in range(cant):
        if(aux):
            x_2.append('1')
            aux=False
        else: 
            x_2.append('-1')
            aux=True
    if(str(operacion).count("AND")):
        x_Correctos.append('1')
        x_Correctos.append('-1')
        x_Correctos.append('-1')
        x_Correctos.append('-1')
    if(str(operacion).count("OR")):
        x_Correctos.append('1')
        x_Correctos.append('1')
        x_Correctos.append('1')
        x_Correctos.append('-1')
    if(str(operacion).count("XOR")):
        x_Correctos.append('-1')
        x_Correctos.append('1')
        x_Correctos.append('1')
        x_Correctos.append('-1')
def Calculando (x_0,x_1,x_2,x_Correctos,w_0,w_1,w_2,listaPesos):
    conerror=True
    for i,correcto in enumerate(x_Correctos):
        y=(w_0*int(x_0[i]))+(w_1*int(x_1[i]))+(w_2*int(x_2[i]))
        print("w0= ",w_0,"w1=",w_1,"w2=",w_2)
        pesos(y,x_0[i],x_1[i],x_2[i],w_0,w_1,w_2,correcto,listaPesos)

def reCal (w0,w1,w2,error,x0,x1,x2,correcto,listaPesos):
    w0=w0+((.04)*error*int(x0))
    w1=w1+((.04)*error*int(x1))
    w2=w2+((.04)*error*int(x2))
    y=(w0*int(x0))+(w1*int(x1))+(w2*int(x2))
    print("w0= ",w0,"w1=",w1,"w2=",w2)
    pesos(y,x0,x1,x2,w0,w1,w2,correcto,listaPesos)
    


def pesos (y,x0,x1,x2,w0,w1,w2,correcto,listaPesos):
    bandera=True
    while bandera:
        print("antes que entre: ",y)
       
        if(y>=0):
            y2=1
        else:
            y2=-1
        error=int(correcto)-(y2)
        if error == 0:
            print(x0,'\t',x1,'\t',x2,'\t',y2,'\t',error,'\t',y)
            listaPesos.append(y)
            listaErrores.append(error)
            listaY2.append(y2)

            bandera=False
        else:
            reCal(w0,w1,w2,error,x0,x1,x2,correcto,listaPesos)
            bandera=False

bol=True
while bol:            
    
    try:
        print("Selecciona que operador lògico deseas:  AND , OR, XOR ")
        operador=input()
        Modificacion_1(4,aux,operador,x_Correctos)
        w_0=random.uniform(-1.5,1.5)
        w_1=random.uniform(-1.5,1.5)
        w_2=random.uniform(-1.5,1.5)
        Calculando(x_0,x_1,x_2,x_Correctos,w_0,w_1,w_2,listaPesos)
        print(listaPesos)
        df = pd.DataFrame()
        df['x0'] = x_0
        df['x1']= x_1
        df['x2']= x_2
        df['yD']= listaY2
        df['error']=listaErrores
        df['peso']=listaPesos
        print(tabulate(df,headers=["x0", "x1","x2","YD","error","peso"],tablefmt='fancy_grid'))
        print("Desas Continuar ? Y / N")
        cnt=input()
        if(cnt.count('Y')):
            bol=True
            operador=''
            x_0=[]
            x_1=[]
            x_2=[]
            listaY2=[]
            listaErrores=[]
            listaPesos=[]
            x_Correctos=[]
        if(cnt.count('N')):
            bol=False
    except :
        print("Ingresa valores correctos")
        print("Desas Continuar ? Y / N")
        cnt=input()
        if(cnt.count('Y')):
            bol=True
            operador=''
            x_0=[]
            x_1=[]
            x_2=[]
            listaY2=[]
            listaErrores=[]
            listaPesos=[]
            x_Correctos=[]
        if(cnt.count('N')):
            bol=False
    