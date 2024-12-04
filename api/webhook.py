from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>TOSbot</title></head>
        <body>
            <h1>Welcome to TOSbot</h1>
            <p>This is the default landing page for TOSbot.</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
