from flask import Flask, render_template, flash, request, redirect, send_from_directory, url_for
import os



app = Flask (__name__)
app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = 'upload'

@app.route("/", methods=["GET", "POST"])
	return redirect ('/cabinet')

@app.route("/cabinet", methods=['GET', 'POST'])

def cabinet():
	return render_template('cabinet.html')

def upload_file():
    if request.method == "POST":
        ff = request.files['file']
        ff.save(os.path.join(app.config['UPLOAD_FOLDER'], ff.filename))
    return redirect(url_for('uploaded_file', filename=filename))

@app.route("/upload/<filename>")
def uploaded_file (filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/favicon.ico')
def favicon():
	return send_from_directory("static", "favicon.ico", mimetype="image/vnd.microsoft.icon")

if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)

