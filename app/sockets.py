from flask_socketio import SocketIO

socketio = SocketIO()

@socketio.on('connect')
def test_connect():
    print('Client connected')

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')
