from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get("http://exampleservice1:8082/?language=Python").content
    return 'Hey, we have Flask in a Docker container!' + r

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8001)