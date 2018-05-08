from flask import Flask, render_template, request
from chatbot import Chatbot


app = Flask(__name__)

bot = Chatbot()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    bot.initialize()
    userText = request.args.get('msg')
    print(userText)
    print(type(userText))
    return str(bot.chat(userText))


if __name__ == "__main__":
    app.run(debug=True, threaded=False)
