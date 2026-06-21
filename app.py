from flask import Flask, render_template, request

app = Flask(__name__)

ai_data = {
    "hello": "Hey! How can I help you?",
    "hi": "Hello there!",
    "what is python": "Python is a powerful programming language.",
    "who is nabi": "Nabi Ahmad is a Software Developer and Full Stack Developer.",
    "bye": "Goodbye! Have a great day!"
}

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""

    if request.method == "POST":
        user = request.form["message"].lower().strip()
        response = ai_data.get(user, "Sorry, I don't understand.")

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)