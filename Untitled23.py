#!/usr/bin/env python
# coding: utf-8

# In[2]:


import plotly.express as px
import streamlit as st
import pandas as pd
df = pd.read_csv('toy_dataset.csv')
Fig1 = px.bar(df, x= 'Gender', y = 'Income', title = 'Bar plot depicting Income based on Gender')
Fig2= px.box(df, x= 'Gender', y = 'Age', title = 'Box plot depicting age based on Gender')
st.plotly_chart(Fig1)
st.plotly_chart(Fig2)
st.markdown("## Detailed Data table View")
st.dataframe(df)


# In[ ]:





# In[ ]:




