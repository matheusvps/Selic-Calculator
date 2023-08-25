import numpy as np
import json
from datetime import timedelta, date, datetime
import csv
import pandas as pd
import dados

#Durante feriados e finais de semana, a taxa SELIC não foi alterada. Para que os cálculos estejam corretos, será necessário adotar a primeira taxa anterior à data dita, utilizando-a ao calcular os juros compostos .

f = open('dados.json')

data = json.load(f)

def getDate(i): #Essa função percorre toda a database e separa ela em colunas, retornando a data no índice i em formatos separados .
  d = data[i]['data'].split('/')
  dt = date(int(d[2]), int(d[1]), int(d[0]))
  return dt

def getRate(date): #Se a data existe (no modelo da database, feriados e finais de semana não foram inclusos), a função getRate retorna a taxa Selic diária daquele dia .
  i = 0
  while getDate(i) <= date:  # Vai até a 1a data maior que a procurada    
    i += 1
  i -= 1
  if(getDate(i) == date):
    return float(data[i]['valor'])
  else:
    return 0

def existeData(date):
  i = 0
  while getDate(i) <= date:  # Vai até a 1a data maior que a procurada    
    i += 1
  i -= 1
  if(getDate(i) == date):
    return True
  else:
    return False
  

d = int(input("Dia Ini: "))
m = int(input("Mes Ini: "))
a = int(input("Ano Ini: "))
dataInicial = date(a, m, d)

d = int(input("Dia Fim: "))
m = int(input("Mes Fim: "))
a = int(input("Ano Fim: "))
dataFinal = date(a, m, d)

def calcularGanho(d1, d2, capital):  # Calcula o ganho entre data 1 e data 2
  dt = d1
  lista = []
  capitalAnt = capital
  while dt <= d2:
    if(existeData(dt)):
      lista.append(tuple([dt, capital, capitalAnt])) #Acumula os ganhos na lista .
    capitalAnt = capital
    capital *= 1 + (getRate(dt) * 0.01)
    dt += timedelta(days=1)

  return lista

#lst = calcularGanho(dataInicial, dataFinal, 657.43)

#Respondendo ao questionamento sobre os 500 dias mais rentáveis : 

intervalos = []

for j in range(0,len(getDate(data)),500):
  intervalos.append(calcularGanho(getDate(j), getDate(j+500), 100))


maiorvalor = max(intervalos)
print(maiorvalor)
f.close() 
