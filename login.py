from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # セッションデータの暗号化に使われるキー

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
    return render_template('dashboard.html', username=session['user'])

if __name__ == '__main__':
    app.run(debug=True)
