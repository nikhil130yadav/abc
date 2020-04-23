from flask import Flask,jsonify,redirect
from chatbotfinal import Session

app = Flask(__name__)
session = Session()


@app.route("/",methods=["GET"])
def base():
    return redirect("/chat")


@app.route("/chat",methods=["GET"])
@app.route("/chat/",methods=["GET"])
def Welcome():
    result = "BOT: Welcome Guest \n Hi! How may I assist you?"
    
    return result


@app.route("/chat/<inp>",methods=["GET"])
def chat(inp):
    if(str(inp)=='res'):
        return redirect("/chat")
    
    result = session.reply(str(inp))
    return result
if __name__== '__main__':
    app.run(host="localhost",port=5000,debug=False)