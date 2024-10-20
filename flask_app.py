from flask import Flask, render_template
import asyncio
from websockets.sync.client import connect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message/<message>')
def send_message(message):
    response = communicate_with_websocket(message)
    return response

def communicate_with_websocket(message):
    with connect("ws://localhost:8765") as websocket:
        websocket.send(message)
        return websocket.recv()

if __name__ == "__main__":
    app.run(debug=True)
