from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', endpoint='index')
def home():
    return render_template('index.html')


@app.route('/authentication')
def authentication():
    return render_template('lics-authentication.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)