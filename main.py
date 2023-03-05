from openchat import create_app
from flask_cors import CORS
from flask_socketio import SocketIO
import os

app = create_app()
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__':
    app.run(debug=True)
    socketio = SocketIO(app, cors_allowed_origins="*")
    socketio.run(app, host='0.0.0.0', port=port, allow_unsafe_werkzeug=True)