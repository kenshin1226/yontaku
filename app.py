
#from flask import Flask,render_template,request				#Flaskをインポート
from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3
import bcrypt

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




# SQLite3データベース接続設定
def create_db_connection():
    connection = sqlite3.connect('yontakudatabase.db')
    return connection
# ユーザーの認証を行う関数
def authenticate_user(username, password):
    connection = create_db_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = "SELECT pass FROM users WHERE name = ?"
            cursor.execute(query, (username))
            result = cursor.fetchone()
            print(f"{result=}")
            if result:
                hashed_password = result[0]
                if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                    return True
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
        finally:
            cursor.close()
            connection.close()
    return False
# with open('quiz_questions.txt', 'r', encoding='utf-8') as file:
#     content = file.read().strip()
# questions = content.split('\n\n')
# quiz_questions = []
# for question in questions:
#     parts = question.split('\n')
#     if len(parts) == 6:
#         quiz_questions.append(parts)



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['user'] = username       #{'username':'kkk'}
            return redirect(url_for('syutudai'))
        else:
            # return render_template('error.html')  # ログイン失敗時にerror.htmlを表示
            return "エラー"
    return render_template('login.html')



# # 固定のユーザー情報を定義
# USER_CREDENTIALS = {
#     "sugizaki": "kensin"
# }

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     error_message = None

#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')



#         hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#         connection = create_db_connection()
#         if connection is not None:
#             try:
#                 cursor = connection.cursor()
#                 query = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
#                 cursor.execute(query, (username, hashed_password))
#                 connection.commit()
#                 cursor.close()
#                 connection.close()
#                 return True
#             except sqlite3.Error as e:
#                 print(f"The error '{e}' occurred")
#             finally:
#                 cursor.close()
#                 connection.close()
               
#         byte=password.encode()
#         hashed_password=bcrypt.hashpw(byte, bcrypt.gensalt())
#         print(f"{hashed_password=}")
#         # データを確認
#         conn = sqlite3.connect('yontakudatabase.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE name=? AND pass=?", (username, hashed_password))
#         rows = cursor.fetchall()
#         print(f"{rows=}")
#         conn.close()
        

        
#         if rows==[]:
#             error_message = 'Login Unsuccessful. Please check username and password'
#         else:
#             session['user'] = username
#             return redirect(url_for('dashboard'))

#     return render_template('login.html', error_message=error_message)

@app.route('/regist',methods=['GET','POST'])
def regist():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        byte=password.encode()
        hashed_password = bcrypt.hashpw(byte, bcrypt.gensalt())
        age=10
        seibetu='男'
        conn = sqlite3.connect('yontakudatabase.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age, pass,seibetu) VALUES(?,?,?,?) ",(username, age,hashed_password,seibetu))
        conn.commit()
        # データを確認
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        for row in rows: 

            print(row)
        
        

        # 接続を閉じる
        conn.close()    
    return render_template('regist.html')


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
