from flask import Flask, request, jsonify
from cipher.transposition import TranspositionCipher

app = Flask(__name__)
cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')
    if not text or not isinstance(key, int):
        return jsonify({'error': 'Invalid input'}), 400
    encrypted = cipher.encrypt(text, key)
    return jsonify({'encrypted_text': encrypted})

@app.route('/api/transposition/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    text = data.get('text')
    key = data.get('key')
    if not text or not isinstance(key, int):
        return jsonify({'error': 'Invalid input'}), 400
    decrypted = cipher.decrypt(text, key)
    return jsonify({'decrypted_text': decrypted})

if __name__ == '__main__':
    app.run(debug=True)
