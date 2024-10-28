import streamlit as st
import time

st.title("BrainFuck林もも")
text = st.text_input("Your BrainFuck林もも here", "ママでちゅよ")

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")

cells = [0] * 256
cursol=0

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

    while cursol<=len(yuuhayashi):
        time.sleep(0.2)
        st.write("ありはやし")

    st.write(cells)
    st.write(cells[9])
    cells=[0] * 256





st.write('デバッグエリア')
st.write(text)
st.write(yuuhayashi)