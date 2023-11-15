import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("data.csv")
st.title("RAJKUMAR")
if st.sidebar.button("load dataset"):
    st.write(df)
    
if st.sidebar.button("show graph"):
    df2=df.head()
    fig=plt.figure(figsize=(10,8))
    plt.bar(df2['sl'],df2["trade"])
    st.pyplot(fig)

if st.sidebar.button("scatter plot"):
    df2=df.head()
    fig=plt.figure(figsize=(10,8))
    plt.scatter(df2['sl'],df2["trade"])
    plt.xlabel("sl",fontsize=15)
    plt.ylabel("trade",fontsize=15)
    st.pyplot(fig)
