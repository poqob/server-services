from flask import Flask, render_template

app = Flask(__name__, static_folder='content', template_folder='templates')  # This tells Flask where templates and static content are located

# Static dosyalara URL ulaşımını düzenleyen özel URL kuralı
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

@app.route('/irme')
def love():
    return render_template('irme.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)