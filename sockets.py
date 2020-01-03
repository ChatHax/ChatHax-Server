from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('message', namespace='/test')
def handle_message(message):
    print('received message: ' + message)
    return render_template('test.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    send('ChatHax-Server: Websocket connection initiated'})
    return render_template('test.html')

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    return render_template('test.html')

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0')