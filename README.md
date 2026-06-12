<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=Caesar%20Cipher%20Tool&fontSize=50&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Task-01%20%7C%20Python%20%2B%20Flask%20%7C%20Encrypt%20%26%20Decrypt&descAlignY=55&descSize=16" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> ### 🔐 *A beautiful, animated web-based Caesar Cipher tool — encrypt and decrypt secret messages with a 3D particle background, running entirely on your local machine.*

<br/>

</div>

---

## 📸 Preview

<!-- Replace this with your actual screenshot -->
<div align="center">
<img src="screenshot.png" alt="Caesar Cipher Tool UI" width="90%" style="border-radius: 12px; box-shadow: 0 8px 32px rgba(0,0,0,0.4);"/>
</div>

> 📌 *To add your screenshot: take a screenshot of `localhost:5000`, save it as `screenshot.png` in the project root.*

---

## ✨ Features

<table>
  <tr>
    <td align="center" width="200">🔒<br/><b>Encrypt</b><br/><sub>One-click message encryption with custom shift</sub></td>
    <td align="center" width="200">🔓<br/><b>Decrypt</b><br/><sub>Instantly decode any Caesar-ciphered text</sub></td>
    <td align="center" width="200">🔍<br/><b>Brute Force</b><br/><sub>Try all 25 shifts at once to crack unknown ciphers</sub></td>
  </tr>
  <tr>
    <td align="center">🎚️<br/><b>Shift Slider</b><br/><sub>Interactive 1–25 shift selector with live preview</sub></td>
    <td align="center">🔤<br/><b>Alphabet Map</b><br/><sub>Full A→Z visual mapping with highlighted active letters</sub></td>
    <td align="center">✨<br/><b>3D Particle BG</b><br/><sub>Live starfield that reacts to mouse movement</sub></td>
  </tr>
  <tr>
    <td align="center">📊<br/><b>Live Stats</b><br/><sub>Character count, letters shifted, shift used</sub></td>
    <td align="center">📋<br/><b>Copy Output</b><br/><sub>One-click copy with green flash confirmation</sub></td>
    <td align="center">⌨️<br/><b>Keyboard</b><br/><sub>Ctrl+Enter shortcut to process message</sub></td>
  </tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

Make sure you have **Python 3** installed on your system.

```bash
python --version   # Should be 3.x
```

### Installation & Run

```bash
# 1. Clone or download the project
git clone https://github.com/enthem-nitishh/caesar-cipher-tool.git
cd caesar-cipher-tool

# 2. Install the only dependency
pip install flask

# 3. Start the server
python app.py

# 4. Open in your browser
# → http://localhost:5000
```

> ✅ That's it! No complex setup, no build tools, no database.

---

## 📁 Project Structure

```
caesar_cipher/
│
├── 📄 app.py                ← Flask backend · cipher logic · API routes
├── 📄 requirements.txt      ← Python dependencies (just Flask)
├── 📄 README.md             ← This file
│
└── 📁 templates/
    └── 📄 index.html        ← Full animated frontend (HTML + CSS + JS)
```

---

## 🔬 How Caesar Cipher Works

The Caesar Cipher is one of the oldest and simplest encryption techniques. Each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

```
Plaintext:   H  E  L  L  O     W  O  R  L  D
Shift:       +3 +3 +3 +3 +3    +3 +3 +3 +3 +3
Ciphertext:  K  H  O  O  R     Z  R  U  O  G
```

**Formula:**

```
Encrypt:  C = (P + shift) mod 26
Decrypt:  P = (C - shift) mod 26
```

- Letters are shifted, spaces and symbols stay unchanged
- Wraps around the alphabet (Z + 3 = C)
- Case is preserved (uppercase stays uppercase)

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/` | Serves the main UI |
| `POST` | `/process` | Encrypt or decrypt a message |
| `POST` | `/brute` | Try all 25 shifts on a message |

### `/process` — Request Body

```json
{
  "text": "Hello World",
  "shift": 3,
  "mode": "encrypt"
}
```

### `/process` — Response

```json
{
  "output": "Khoor Zruog",
  "original": "Hello World",
  "shift": 3,
  "mode": "encrypt",
  "alphabet": ["A", "B", "C", "..."],
  "shifted":  ["D", "E", "F", "..."],
  "char_count": 11,
  "letter_count": 10,
  "word_count": 2
}
```

---

## 🛠️ Tech Stack

| Technology | Role |
|------------|------|
| **Python 3** | Core language |
| **Flask** | Web server & API |
| **HTML5 + CSS3** | Animated frontend UI |
| **Vanilla JavaScript** | Interactivity, fetch API |
| **Canvas API** | 3D particle background |
| **Google Fonts** | Syne + JetBrains Mono typography |

---

## 📊 Project Stats

```
Lines of Python  →  ~60
Lines of HTML    →  ~800+
Shift Values     →  25
Cipher Modes     →  2 (Encrypt / Decrypt)
Bonus Features   →  Brute Force cracker
```

---

## 🎯 Task Checklist

- [x] Python program to encrypt text using Caesar Cipher
- [x] Python program to decrypt text using Caesar Cipher
- [x] User can input a message
- [x] User can choose a custom shift value (1–25)
- [x] Web-based UI running on localhost
- [x] Attractive animated interface with 3D background
- [x] **Bonus:** Brute Force cracker (try all 25 shifts)
- [x] **Bonus:** Alphabet mapping visualization
- [x] **Bonus:** Live statistics (char count, word count, etc.)

---

## 👨‍💻 Author

<div align="center">

**Made with ❤️ for Task-01**

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/enthem-nitishh)

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
