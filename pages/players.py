import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit  as st 
df = pd.read_csv(r"fifa_eda.csv")
df.dropna(inplace=True)
st.title('Players')
sum = df["Name"].count()
st.write("sum of players ", sum)
selection = st.selectbox("select", df.select_dtypes(include="number").columns)
mydf = df.nlargest(10 ,selection)[['Name' , 'Club' , selection ]]
fig  = px.bar(mydf , x ="Name" , y = selection )
st.plotly_chart(fig)
max_value = df[selection].max()
min_value  = df[selection].min()
mean_value = int(df[selection].mean())
col_1,col_2 , col_3= st.columns(3)
card = col_1.container(border=1)
card2 = col_2.container(border = 1 )
card3 = col_3.container(border = 1 )
card.metric(label=f'max' , value=max_value)
card2.metric(label=f'min' , value=min_value)
card3.metric(label=f'mean' , value=mean_value)
st.markdown(df["Name"].to_markdown(index= False))



