import pandas as pd 
import numpy as np 
import plotly.express as px 
import streamlit  as st 
df = pd.read_csv(r"../fifa_eda.csv")
df.dropna(inplace=True)
st.title('Club')
sum = df["Name"].count()
st.write("sum of club ", sum)
club_count = df.groupby("Club")['Name'].count().reset_index()
vis_club_count = px.bar(club_count, x="Club", y="Name", title="Number of Players per Club")

st.plotly_chart(vis_club_count)
st.dataframe(club_count)
