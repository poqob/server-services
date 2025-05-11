from flask import Flask, render_template, jsonify, send_from_directory
import os
import random
from src.zorba import kufurler

# Create Flask application with explicit folder configurations
app = Flask(__name__, 
           template_folder='templates')

# Main route to serve the HTML page
@app.route('/zorba')
def serve_zorba():
    return render_template('zorba.html')

# Routes to serve static files from the templates directory
@app.route('/zorba/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

# API endpoint to serve random "kufur"
@app.route('/zorba-api')
def serve_zorba_api():
    # Rastgele bir küfür seç
    secilen_kufur = random.choice(kufurler)
    return jsonify({"kufur": secilen_kufur})

if __name__ == '__main__':
    # Using a different port than the default 5000 to avoid conflicts
    app.run(host='127.0.0.1', port=5000)
