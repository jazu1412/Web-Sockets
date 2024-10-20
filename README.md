
# WebSocket Chat Application

This is a WebSocket-based chat application that demonstrates real-time, full-duplex communication between a client and a server. The server modifies each message by appending a random number before sending it back to the client. A modern user interface is built using HTML, CSS, and JavaScript, while the backend is handled by Flask and Python.

## Key Features

- **Full-Duplex Communication:** Utilizes the WebSocket protocol for real-time two-way communication between client and server.
- **Random Number Addition:** The server appends a random number to the client's message before sending it back.
- **Modern UI:** The chat interface is styled to resemble modern chat applications, with different colors for sent and received messages.

## How It Works

1. The client sends a message to the WebSocket server.
2. The server receives the message, appends a random number to it, and sends it back.
3. The client displays both the sent message and the received message in a chat-like UI.

## Setup and Installation

1. **Install Dependencies:**
    ```bash
    pip install websockets flask
    ```

2. **Run the WebSocket Server:**
    ```bash
    python3 modified_websocketserver.py
    ```

3. **Run the WebSocket Client:**
    ```bash
    python3 modified_websocketclient.py
    ```

4. **Run the Flask App for the UI:**
    ```bash
    python3 flask_app.py
    ```

5. **Access the Web App:**  
   Open your browser and navigate to `http://127.0.0.1:5000/` to use the chat interface.


## Conclusion

This WebSocket chat application demonstrates efficient, real-time communication using the WebSocket protocol. It showcases the ease of using WebSockets for full-duplex communication and offers a clean, intuitive user interface for seamless interaction.
