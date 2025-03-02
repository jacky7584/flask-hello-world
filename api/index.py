from flask import Flask, request, jsonify
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/pdf', methods=['POST'])
def pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return jsonify({'text': text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
