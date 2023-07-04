from flask import Flask

# フラスクのインスタンス化
app = Flask(__name__)

# ルートディレクトリにアクセスした時の処理
@app.route('/')
def hello():
    return 'Hello World!'

# エントリーポイント
if __name__ == '__main__':
    app.run()

