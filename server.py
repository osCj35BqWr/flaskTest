from flask_blog import app

if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    # デバックモードでアプリを起動
    # app.run(debug=True)
    # 本番
    # app.run()
    # host='0.0.0.0'を指定しないと、サーバーは公開されない
    # ※「Flaskのサーバーはデフォルトだと公開されてない」
    # https://qiita.com/tomboyboy/items/122dfdb41188176e45b5
    app.run()
