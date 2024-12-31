from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to 2025!\n We're so glad you're here to celebrate the new year!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
