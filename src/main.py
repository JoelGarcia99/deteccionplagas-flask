from flask import Flask, jsonify
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, host="192.168.0.103", port=5000)
    socketio.init_app(app, cors_allowed_origins="*")

@socketio.on('connect')
def socket_connection():
    return jsonify({
        "status": "Socket is active"
    })