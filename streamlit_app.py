import streamlit as st
import time

st.title("BrainFuck林もも")
text = st.text_input("Your BrainFuck林もも code here", "ママでちゅよおっぱいおっぱいボロンママでちゅよおっぱい")
input = st.text_input("標準入力(ありばや進数で入力してください)","外星人かわいい")

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")

cells = [0] * 256
cursol=0
workinghayashi=0
nyuuryokubayashi=0
output=""

yuuhayashi=text
yuuhayashi=yuuhayashi.replace('ママでちゅよ', '右')
yuuhayashi=yuuhayashi.replace('有林', '左')
yuuhayashi=yuuhayashi.replace('おっぱい', '足')
yuuhayashi=yuuhayashi.replace('ボロン', '引')
yuuhayashi=yuuhayashi.replace('妹ちゃん', '出')
yuuhayashi=yuuhayashi.replace('護法2', '入')
yuuhayashi=yuuhayashi.replace('アピールしてください', '恥')
yuuhayashi=yuuhayashi.replace('こんもも', '終')

if on:
    while cursol<=(len(yuuhayashi)-1):
        time.sleep(0.2)
        if yuuhayashi[cursol]=="右":
            workinghayashi=workinghayashi+1
            if workinghayashi==256:workinghayashi=0
            cursol=cursol+1
        elif yuuhayashi[cursol]=='左':
            workinghayashi=workinghayashi-1
            if workinghayashi==-1:workinghayashi=255
            cursol=cursol+1
        elif yuuhayashi[cursol]=='足':
            cells[workinghayashi]=cells[workinghayashi]+1
            if cells[workinghayashi]==256:cells[workinghayashi]=0
            cursol=cursol+1
        elif yuuhayashi[cursol]=='引':
            cells[workinghayashi]=cells[workinghayashi]-1
            if cells[workinghayashi]==-1:cells[workinghayashi]=255
            cursol=cursol+1
        elif yuuhayashi[cursol]=='出':
            cursol=cursol+1
        elif yuuhayashi[cursol]=='入':
            cursol=cursol+1


    st.write(cells)
    st.write(cells[9])
    st.write(output)
    st.write("180秒後にもう一周します")
    time.sleep(180)
    cells=[0] * 256




st.write('デバッグエリア')
st.write(text)
st.write(yuuhayashi)