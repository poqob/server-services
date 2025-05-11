from flask import Flask, render_template, send_from_directory

# Create Flask application with explicit folder configurations
app = Flask(__name__, 
           template_folder='templates')

# Main route to serve the HTML page
@app.route('/irme')
def love():
    return render_template('irme.html')

# Routes to serve static files from the templates directory
@app.route('/irme/<path:filename>')
def serve_static(filename):
    return send_from_directory('templates', filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003)