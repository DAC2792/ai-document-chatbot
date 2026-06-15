from flask import Flask, render_template, request
import anthropic
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    document = request.form.get("document")
    question = request.form.get("question")

    message = client.messages.create(
        model = "claude-sonnet-4-6",
        max_tokens = 1024,
        messages=[
            {"role":"user", "content":f"Document: {document}\n\nQuestion: {question}"}
        ]
    )
    return render_template("index.html", answer=message.content[0].text)

if __name__ == "__main__":
    app.run(debug=True)