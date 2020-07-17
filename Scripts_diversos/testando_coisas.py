import numpy as np
from pandas import DataFrame

dados = {'campeões': ['shyvana','rammus','braum','xin zhao','poppy'],
         'abates':[4,4,1,18,17],
         'mortes':[7,11,5,15,15],
         'assistências':[12,29,23,13,29]}

frame = DataFrame(dados)

frame2 = DataFrame(dados, columns = ['campeões','abates','mortes','assistências','KDA'])

frame2['KDA'] = (np.array(dados['abates'])+np.array(dados['assistências']))/np.array(dados['mortes'])

print(frame)
print(frame2)

