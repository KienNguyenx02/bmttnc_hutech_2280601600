from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

@app.route('/caesar/encrypt', methods=['POST'])
def encrypt_caesar():
    data = request.json
    text = data['text']
    shift = int(data['shift'])
    return jsonify({'result': caesar_encrypt(text, shift)})

@app.route('/caesar/decrypt', methods=['POST'])
def decrypt_caesar():
    data = request.json
    text = data['text']
    shift = int(data['shift'])
    return jsonify({'result': caesar_decrypt(text, shift)})

if __name__ == '__main__':
    app.run(port=5000)
