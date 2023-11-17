from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/test')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run("0.0.0.0", port=5500)