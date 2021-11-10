from flask import Flask
import debugpy

debugpy.listen(('0.0.0.0', 5678))
debugpy.wait_for_client()

server = Flask(__name__)

@server.route("/")
def home():
    return "<p>Wazzup?</p>"

if __name__ == "__main__":
    server.run(debug=True, host='0.0.0.0', port=5000)