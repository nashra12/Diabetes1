from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello Nashra, World!</h1>"
    #here we can write anything

if __name__=="__main__":
    app.run(host="0.0.0.0")
