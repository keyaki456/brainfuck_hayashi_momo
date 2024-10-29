import streamlit as st
import time

st.title("BrainFuck林もも")
text = st.text_area("Your BrainFuck林もも code here", "おっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱい妹ちゃんボロンボロンボロン妹ちゃんおっぱいおっぱいおっぱいおっぱいおっぱいおっぱいおっぱい妹ちゃん妹ちゃんおっぱいおっぱいおっぱい妹ちゃん")
input = st.text_input("標準入力(ありばや進数で入力してください)","外星人かわいい")

on = st.toggle("←runボタン。これがonの間、有林が働き続ける。")

cells = [0] * 256
cursol=0
workinghayashi=0
nyuuryokubayashi=0
output=""
tmpcount=0

aribayashiturple=("0","1","2","3","4","5","6","7","8","9",
                  "a","b","c","d","e","f","g","h","i","j",
                  "k","l","m","n","o","p","q","r","s","t",
                  "u","v","w","x","y","z","A","B","C","D",
                  "E","F","G","H","I","J","K","L","M","N",
                  "O","P","Q","R","S","T","U","V","W","X",
                  "Y","Z","あ","い","う","え","お","か","き","く",
                  "け","こ","さ","し","す","せ","そ","た","ち","つ",
                  "て","と","な","に","ぬ","ね","の","は","ひ","ふ",
                  "へ","ほ","ま","み","む","め","も","や","ゆ","よ",
                  "ら","り","る","れ","ろ","わ","を","ん","有","林",
                  "栗","川","羅","生","門","清","楚","淫","乱","妹",
                  "緑","単","相","撲","ア","イ","ウ","エ","オ","カ",
                  "キ","ク","ケ","コ","サ","シ","ス","セ","ソ","タ",
                  "チ","ツ","テ","ト","ナ","ニ","ヌ","ネ","ノ","ハ",
                  "ヒ","フ","屁","ホ","マ","ミ","ム","メ","モ","ヤ",
                  "ユ","ヨ","ラ","リ","ル","レ","ロ","ワ","ヲ","ン",
                  "外","星","人","激","怒","邪","智","暴","虐","芋",
                  "粥","作","業","枠","飲","酒","雑","談","甘","藍",
                  "ど","寝","前","過","呼","吸","更","配","信","者",
                  "達","質","問","箱","会","話","幻","塔","長","距",
                  "離","運","送","ー","ガ","ギ","グ","ゲ","ゴ","ザ",
                  "ジ","ズ","ゼ","ゾ","ダ","ヂ","ヅ","デ","ド","バ",
                  "美","ブ","ベ","ボ","パ","ピ","プ","ペ","ポ","肉",
                  "少","女","が","ぎ","ぐ","げ","ご","ざ","じ","ず",
                  "ぜ","ぞ","だ","ぢ","づ","で")

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
            output=output+aribayashiturple[cells[workinghayashi]]
            cursol=cursol+1
        elif yuuhayashi[cursol]=='入':
            for i in range(len(aribayashiturple)):
                if aribayashiturple[i]==input[nyuuryokubayashi]:
                    cells[workinghayashi]=i
                    break
            nyuuryokubayashi=nyuuryokubayashi+1
            if nyuuryokubayashi>len(input)-1:
                nyuuryokubayashi=len(input)-1
            cursol=cursol+1
        elif yuuhayashi[cursol]=='恥':
            if cells[workinghayashi]==0:
                tmpcount=1
                while tmpcount>0 and cursol<=(len(yuuhayashi)-1):
                    cursol=cursol+1
                    if yuuhayashi[cursol]=='恥':tmpcount=tmpcount+1
                    if yuuhayashi[cursol]=='終':tmpcount=tmpcount-1
                cursol=cursol+1
            else:
                cursol=cursol+1
        elif yuuhayashi[cursol]=='終':
            if cells[workinghayashi]==0:
                cursol=cursol+1
            else:
                cursol=cursol-1
                tmpcount=1
                while tmpcount>0 and cursol>=0:
                    cursol=cursol-1
                    if yuuhayashi[cursol]=='終':tmpcount=tmpcount+1
                    if yuuhayashi[cursol]=='恥':tmpcount=tmpcount-1
                cursol=cursol+1
                


    st.title("出力")
    st.write(output)
    st.write("(180秒後にもう一周します)")
    time.sleep(180)
    cells=[0] * 256




