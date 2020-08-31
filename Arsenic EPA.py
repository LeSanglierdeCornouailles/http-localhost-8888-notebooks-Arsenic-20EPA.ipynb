#!/usr/bin/env python
# coding: utf-8

# In[478]:


import pandas as pd


# In[479]:


df1 = pd.read_excel (r'C:\Users\v-victgo\Desktop\South Dublin Results 2019.xlsx')


# In[480]:


pd.set_option('display.max_columns', None)


# In[481]:


df1.head(3)


# In[482]:


df1.columns.values


# In[483]:


df2 = pd.read_excel (r'C:\Users\v-victgo\Desktop\South Dublin list of exceedances 2019.xlsx')


# In[484]:


df2.head(3)


# In[485]:


df2.Units.unique()


# In[486]:


df1.columns.values


# In[487]:


frames = [df1, df2]
result = pd.concat(frames)
result.head(3)


# In[488]:


result.columns.values


# In[489]:


result.dtypes


# In[490]:


results = result.rename({'Sample Date': 'Sample_Date'}, axis ='columns')


# In[491]:


results['Sample_Date'] = [d.date() for d in results ['Sample_Date']]


# In[492]:


results.head(3)


# In[ ]:





# In[493]:


results.dtypes


# In[494]:


results['samples_date'] = pd.to_datetime(results['Sample_Date'])


# In[495]:


results.dtypes


# In[496]:


import numpy as np
from bokeh.plotting import figure, output_file, show
from datetime import datetime as dt


# In[497]:


output_file('my_first_graph.html')


# In[498]:


df_arsenic = results.loc[results['Parameter'] == 'Arsenic']


# In[499]:


df_arsenic


# In[500]:


df_arsenic= df_arsenic.assign(Parametric_Value=10)


# In[501]:


df_arsenic


# In[502]:


x = df_arsenic.loc[:,'samples_date']
y = df_arsenic.loc[:,'Result']
z = df_arsenic.loc[:,'Parametric_Value']


# In[503]:


p = figure(plot_height=600, plot_width=1800, x_axis_type='datetime')


# In[504]:


p.circle(x , y, size =10, color='red')
p.line(x , z, line_width =2, color='red', legend_label='Arsenic')


p.yaxis.axis_label = 'Result [ug/l]'
p.xaxis.axis_label = 'samples_date'
p.title.text = 'Plotting level of Arsenic in South Dublin County for 2019 data got from http://erc.epa.ie/safer/downloadValidityCheck.jsp Done by Victor Gonzalez 31/08/2020'


# In[505]:


show(p)


# In[ ]:




