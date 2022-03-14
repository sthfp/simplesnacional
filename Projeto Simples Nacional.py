#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

optante_simples= pd.read_csv("F.K03200$W.SIMPLES.CSV.D20212", header = None, sep = ';')
optante_simples.rename(columns={0 : "CNPJ", 1 : "OptanteSimples", 2 : "Data de Adesão", 3 : "Data de Saída", 4 : "Optante pelo SIMEI", 5 : "Data Adesão SIMEI", 6 :"Data Saída SIMEI"}, inplace=True)
display(optante_simples_CNPJ)


# In[ ]:





# In[ ]:




