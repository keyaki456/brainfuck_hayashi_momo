import streamlit as st

st.title("BrainFuck林もも")
text = st.text_input("Your BrainFuck林もも here", "ママでちゅよ")

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")

yuuhayashi=text
if on:
    yuuhayashi=yuuhayashi.replace('ママでちゅよ', '7')
    yuuhayashi=yuuhayashi.replace('有林', '8')
    yuuhayashi=yuuhayashi.replace('おっぱい', '+')
    yuuhayashi=yuuhayashi.replace('ボロン', '-')
    yuuhayashi=yuuhayashi.replace('妹ちゃん', '.')
    yuuhayashi=yuuhayashi.replace('護法2', ',')
    yuuhayashi=yuuhayashi.replace('アピールしてください', '[')
    yuuhayashi=yuuhayashi.replace('こんもも', ']')



st.write(text)
st.write(yuuhayashi)