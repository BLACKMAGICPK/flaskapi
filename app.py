from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask API is successfully deployed on Render!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}! 👋 Your Flask app is running perfectly."

if __name__ == '__main__':
    app.run()
