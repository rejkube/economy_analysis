#!/usr/bin/env python
# coding: utf-8

import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import seaborn as sns 


st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("CountryForeignExchangeReserves")

df_data=pd.read_csv('COFER_12-27-2020 06-41-57-24.csv')
df_data=df_data.drop(columns=['Status','Unnamed: 7'],axis=1)

#Data cleanup
df_data[['Reserve_Type','Detail_Reserve','Reserve_Unit']]=df_data['Indicator Name'].str.split(",",expand=True)
df_data=df_data.drop(columns=['Indicator Name'],axis=1)

World_Economy=df_data[df_data['Country Name'] == 'World']
World_Economy=World_Economy.drop(columns=['Country Code'],axis=1)
World_Economy[['Time Period','Value','Reserve_Type','Detail_Reserve']].sort_values(['Time Period'],ascending=[True])
currency_reserve=World_Economy[World_Economy.Reserve_Type.isin(['Allocated Reserves'])
                               & World_Economy.Detail_Reserve.str.contains('US Dollars')]
currency_reserve=currency_reserve[['Time Period','Value','Detail_Reserve']].sort_values(['Time Period'],ascending=[True])
currency_reserve['Value']=(currency_reserve['Value']/100000).round(2)
currency_reserve=currency_reserve.set_index('Time Period')
#Plot begin
st.table(currency_reserve)
st.header("World Economy Distribution in USD")
st.subheader("Bar Plot")
currency_reserve.plot(kind='bar')
st.pyplot()

st.subheader("Displot")
sns.displot(currency_reserve['Value'])
st.pyplot()

