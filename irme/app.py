from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')  # Flask'ın varsayılan statik klasör adı 'static'dir

@app.route('/irme')
def love():
    return render_template('irme.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)