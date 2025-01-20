import streamlit as st
import pandas as pd
import streamlit_pandas as sp
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(page_title= "LETREP25", layout= "wide")
st.title('LETREP25 Dashboard' )
st.subheader('Raw Data')
st.text('For the Physician')
df = pd.read_csv('TestData.csv')
df=df.set_index("Hour")

fig, ax= plt.subplots()
ax = df.plot.barh
st.title('Patient ROM Data')
st.bar_chart(df)








