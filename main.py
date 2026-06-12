from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)

    return ''.join(result)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    text = data.get('text', '')
    shift = int(data.get('shift', 3))
    mode = data.get('mode', 'encrypt')

    if not text:
        return jsonify({'error': 'Text cannot be empty'}), 400

    output = caesar_cipher(text, shift, mode)

    # Build shift table for visualization
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shifted_alphabet = ''.join(
        chr((ord(c) - ord('A') + (shift if mode == 'encrypt' else -shift)) % 26 + ord('A'))
        for c in alphabet
    )

    return jsonify({
        'output': output,
        'original': text,
        'shift': shift,
        'mode': mode,
        'alphabet': list(alphabet),
        'shifted': list(shifted_alphabet)
    })


if __name__ == '__main__':
    print("\n🔐 Caesar Cipher Tool is running!")
    print("👉 Open http://localhost:5000 in your browser\n")
    app.run(debug=True, port=5000)