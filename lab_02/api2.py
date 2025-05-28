from flask import Flask, request, jsonify

app = Flask(__name__)

def vigenere_encrypt(text, key):
    key = key.lower()
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift + 26) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

@app.route('/vigenere/encrypt', methods=['POST'])
def encrypt_vigenere():
    data = request.json
    text = data['text']
    key = data['key']
    return jsonify({'result': vigenere_encrypt(text, key)})

@app.route('/vigenere/decrypt', methods=['POST'])
def decrypt_vigenere():
    data = request.json
    text = data['text']
    key = data['key']
    return jsonify({'result': vigenere_decrypt(text, key)})

if __name__ == '__main__':
    app.run(port=5002)
