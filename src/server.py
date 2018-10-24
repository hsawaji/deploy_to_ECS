from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'deploy ECS'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
