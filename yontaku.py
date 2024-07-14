
#from flask import Flask,render_template,request				#Flaskをインポート
from flask import Flask, render_template, redirect, url_for, session, request
app = Flask(__name__)				#インスタンス作成
app.secret_key = 'your_secret_key' # セッションのための秘密鍵を設定
qus=["日本の首都は？","最近すぎざきけんしんがハマったゲームは?","問3","今日の曜日は？"]
ars=[["大阪","東京","福岡","愛知","神奈川"],
     ["ダービースタリオン","ウイニングポスト","マインクラフト","ファイナルファンタジー"],
     ["あ","い","う","え","お"],
     ["月曜日","水曜日","金曜日","土曜日","日曜日"]]
seikais=["東京","ウイニングポスト","う","日曜日"]

# 初期ページのルート 
@app.route('/') 
def index():
    session['current_question'] = 0 # 現在の質問のインデックスを初期化 
    return redirect(url_for('syutudai'))
#出題
@app.route('/syutudai', methods=['GET'])	#/syutudaiにgetメソッドでアクセスされたとき以下実行
def syutudai():							#中身の関数
    if session['current_question']==len(qus):
        return "終了です"
    c=session['current_question']    
    print(f"{c=}")
    q=qus[c]
    a=ars[c]   
    return render_template('syutudai.html',a=a,q=q,c=c)#もともとc=str(c)だったが問題がなさそうなので外した
#答え合わせ
@app.route('/kotaeAwase', methods=['GET'])	#/kotaeAwaseにgetメソッドでアクセスされたとき以下実行
def kotaeAwase():							#中身の関数
    c=session['current_question']    
    kekka=""
    kaitou = request.args.get('q1')
    print(f"{kaitou=}")
    ans=seikais[c]
    if kaitou == ans:
        kekka="正解"
    else:
        kekka="不正解"
    session['current_question'] += 1 # 次の質問に進む 
    print(f"{session['current_question']=}")
    
    return render_template('kotaeAwase.html',kekka=kekka,ans=ans)


if __name__ == "__main__":			#いつものやつｗ
    app.run(debug=True)				#デバッグオンで動かすと、コード変更時に楽なので
