
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
    return redirect(url_for('login'))
#出題
@app.route('/syutudai', methods=['GET'])	#/syutudaiにgetメソッドでアクセスされたとき以下実行
def syutudai():							#中身の関数
    if "user" not in session :
        return redirect(url_for('login'))
    if session['current_question']==len(qus):
        return "終了です"
    c=session['current_question']    
    q=qus[c]
    a=ars[c]   

    return render_template('syutudai.html',a=a,q=q,c=c)#もともとc=str(c)だったが問題がなさそうなので外した
#答え合わせ
@app.route('/kotaeAwase', methods=['GET'])	#/kotaeAwaseにgetメソッドでアクセスされたとき以下実行
def kotaeAwase():							#中身の関数
    if "user" not in session:
        return redirect(url_for('login'))
    c=session['current_question']    
    kekka=""
    kaitou = request.args.get('q1')
    ans=seikais[c]
    if kaitou == ans:
        kekka="正解"
    else:
        kekka="不正解"
    session['current_question'] += 1 # 次の質問に進む 
    
    return render_template('kotaeAwase.html',kekka=kekka,ans=ans)



# 固定のユーザー情報を定義
USER_CREDENTIALS = {
    "sugizaki": "kensin"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            error_message = 'Login Unsuccessful. Please check username and password'

    return render_template('login.html', error_message=error_message)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('syutudai'))





if __name__ == "__main__":			#いつものやつｗ
    app.run(debug=True)				#デバッグオンで動かすと、コード変更時に楽なので
