from flask import Flask, request, jsonify

app = Flask(__name__)

def rail_fence_encrypt(text, key):
    rail = ['' for _ in range(key)]
    dir_down = False
    row = 0

    for char in text:
        rail[row] += char
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        row += 1 if dir_down else -1

    return ''.join(rail)

def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1

    # fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # read the matrix to get text
    result = ''
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        elif row == key - 1:
            dir_down = False
        result += rail[row][col]
        col += 1
        row += 1 if dir_down else -1

    return result

@app.route('/railfence/encrypt', methods=['POST'])
def encrypt_rail():
    data = request.json
    text = data['text']
    key = int(data['key'])
    return jsonify({'result': rail_fence_encrypt(text, key)})

@app.route('/railfence/decrypt', methods=['POST'])
def decrypt_rail():
    data = request.json
    text = data['text']
    key = int(data['key'])
    return jsonify({'result': rail_fence_decrypt(text, key)})

if __name__ == '__main__':
    app.run(port=5001)
