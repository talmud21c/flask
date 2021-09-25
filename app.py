from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>연이 바보</h1>'

if __name__ == "__main__":
		app.run(host='0.0.0.0', port='80', debug=True)