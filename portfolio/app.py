from flask import Flask, send_from_directory, url_for
import os

app = Flask(__name__, static_folder='content')  # Statik dosyaların content klasöründe olduğunu belirtiyoruz

# Static dosyalara URL ulaşımını düzenleyen özel URL kuralı
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/cv')
def download_cv():
    # content klasöründeki cv.pdf dosyasını dön
    return send_from_directory('content', 'mustafa_biçer_resume.pdf')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)