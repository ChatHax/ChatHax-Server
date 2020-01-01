from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from os import system
system('clear')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('ChatHax-Server:', {'connection1:': 'Websocket connection initiated'})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client has disconnected from the server')

if __name__ == '__main__':
    socketio.run(app.run(host='0.0.0.0'))