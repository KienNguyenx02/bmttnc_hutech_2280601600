from flask import Flask, request, jsonify
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.railfence.railfence_cipher import RailFenceCipher  # 👈 Thêm dòng này

app = Flask(__name__)

vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()  # 👈 Thêm dòng này


@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})


# 👇 Thêm hai API cho railfence:
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.json
    plain_text = data['plain_text']
    num_rails = data['num_rails']
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return jsonify({'encrypted_text': encrypted_text})


@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    num_rails = data['num_rails']
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return jsonify({'decrypted_text': decrypted_text})


if __name__ == '__main__':
    app.run(debug=True)
