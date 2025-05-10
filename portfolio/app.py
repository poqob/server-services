from flask import Flask,send_from_directory
import os

app = Flask(__name__)  # This tells Flask where templates are located

@app.route('/cv')
def download_cv():
    # Assuming you have a CV file in a 'files' directory
    return send_from_directory('content', 'cv.pdf')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001)