# ライブラリ呼び出し
from flask import Flask, render_template

# クラス呼び出し
app = Flask(__name__)

# ルーティングを定義
@app.route('/')
def hello_World():
    return 'HelloWorld！'

# /hello(http://127.0.0.1:5000/hello)にアクセスするとsample.htmlの中身が表示される
@app.route('/hello')
def hello():
    return render_template("sample.html")


# デバックモードでアプリを起動
app.run(debug=True)
