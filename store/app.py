from flask import Flask
app = Flask(__name__)

@app.route("/users/<username>")
def hello(username):
        return "ola {}".format(username)


    app.run(host="0.0.0.0", port=80)

