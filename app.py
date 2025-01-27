from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    app.logger.info(f"Request received from {request.remote_addr}")
    return "Hi I Am Hosting My App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
