from flask import Flask, render_template, request
import json
import time

app = Flask(__name__)

temp = {'dev1': 10, 'dev2': 14, 'dev3': 15, 'dev4': 24}

@app.route('/', methods=['GET'])
def get_info():
    return render_template('index.html', data1=temp)

@app.route('/send', methods=['POST'])
def send_data():
    response = request.get_json()
    return "", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, port=3000)