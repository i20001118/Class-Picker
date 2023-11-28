from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {
    "admin": {"password": "adminpass", "name": "管理员", "role": "Admin"},
    "user1": {"password": "password1", "name": "用户一", "role": "Student"},
    "user2": {"password": "password2", "name": "用户二", "role": "Teacher"}
}

@app.route('/', methods=['GET'])
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # POST 請求用於表單繳交
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)

    if user and user['password'] == password:
        # 登入成功，重定向到用戶頁面
        return redirect(url_for('user_profile', username=username))
    else:
        # 登入失敗
        return "登录失败"

@app.route('/user/<username>')
def user_profile(username):
    # 個別用戶資料頁面
    user = users.get(username)
    if user:
        return render_template('student.html', user=user)
    else:
        return '用户不存在', 404

@app.route('/test')
def hello():
    # 測試
    return "Hello, World!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
