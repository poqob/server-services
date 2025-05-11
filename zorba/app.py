from flask import Flask,render_template,jsonify,url_for
import os
import random
from src.zorba import kufurler

app = Flask(__name__, template_folder='templates', static_folder='content',static_url_path='/zorba/content')  # This tells Flask where templates and static content are located

# Static dosyalara URL ulaşımını düzenleyen özel URL kuralı
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/zorba-api')
def serve_zorba_api():
    # Rastgele bir küfür seç
    secilen_kufur = random.choice(kufurler)
    return jsonify({"kufur": secilen_kufur})

@app.route('/zorba')
def serve_zorba():
    return render_template('zorba.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
