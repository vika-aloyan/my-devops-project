from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Получаем имя хоста. Если мы в Docker, это будет ID контейнера.
    hostname = os.uname()[1]
    return f"<h1>Привет! Я работаю внутри Docker-контейнера.</h1><p>Имя контейнера: {hostname}</p>"

if __name__ == '__main__':
    # 0.0.0.0 обязательно для Docker, чтобы пробросить порт
    app.run(host='0.0.0.0', port=5000)