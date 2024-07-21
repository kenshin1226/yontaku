from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッションデータの暗号化に使われるキー

qus=["日本の首都は？","最近すぎざきけんしんがハマったゲームは?","問3","今日の曜日は？"]
ars=[["大阪","東京","福岡","愛知","神奈川"],
     ["ダービースタリオン","ウイニングポスト","マインクラフト","ファイナルファンタジー"],
     ["あ","い","う","え","お"],
     ["月曜日","水曜日","金曜日","土曜日","日曜日"]]
c=0
q=qus[c]
a=ars[c]  
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
            print(f"@21 {session=}")
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
    print(f"{session=}")
    if 'user' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('syutudai'))
if __name__ == '__main__':
    app.run(debug=True)
