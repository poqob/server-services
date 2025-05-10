from flask import Flask, render_template

app = Flask(__name__, static_folder='content', template_folder='templates')  # This tells Flask where templates and static content are located

@app.route('/irme')
def love():
    return render_template('irme.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)