from flask import Flask, jsonify, render_template_string
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
@app.get('/')
def home():
    return render_template_string("<h1>Hello, Flask!</h1>")
@app.get('/api/health')
def health():
    return jsonify(status="ok")
