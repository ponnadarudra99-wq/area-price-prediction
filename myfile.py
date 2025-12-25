import pickle
import streamlit as st

model=pickle.load(open("area.pkl","rb"))

def myf1():
    st.title("area price prediction")
    area=st.number_input("enter the area value...")
    pred=st.button("predict")

    if pred:
       op=model.predict([[area]])
       st.write("price of the area : ",op[0])
 
myf1()
