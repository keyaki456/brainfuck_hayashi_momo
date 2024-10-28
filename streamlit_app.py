import streamlit as st

st.title("BrainFuck林もも")
yuuhayashi = st.text_input("Your BrainFuck林もも here", "ママでちゅよ")

on = st.toggle("←これがonの間、有林が働き続ける")


a=0
if on:
    st.write("Feature activated!")
    a=a+1


st.write(a)
