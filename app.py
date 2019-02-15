from flask import Flask

app = Flask(__name__)

@app.route('/users')
def index():
    return {1: "user1"}

if __name__ == '__main__':
    app.run()

