from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask API is successfully deployed on Render!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}! 👋 Your Flask app is running perfectly."

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
