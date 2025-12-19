from flask import Flask, request, jsonify
from cipher import encrypt, decrypt  # your logic

app = Flask(__name__)

@app.get("/")
def home():
    return "Vigenere Cipher API"

@app.post("/encrypt")
def do_encrypt():
    data = request.json
    return jsonify({"cipher": encrypt(data["text"], data["key"])})

@app.post("/decrypt")
def do_decrypt():
    data = request.json
    return jsonify({"plain": decrypt(data["cipher"], data["key"])})

if __name__ == "__main__":
    app.run(debug=True)
