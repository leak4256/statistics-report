
import os
from flask import Flask, render_template, send_file, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
from statistics import CreateReportFile
import os


'''allocated flask object'''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = ''
ALLOWED_EXTENSIONS = set(['txt'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def load():
    """loud the form to fill the properties"""
    return render_template('home.html')


@app.route("/<path:filename>", methods=['GET', 'POST'])
def  download(filename=None):
    try:
        path = os.path.join(app.root_path, filename)
        return send_file(path, as_attachment=True)
    except Exception as e:
        return 'f<h1>{e}</h1>'


# ToDo
# @app.route("/<path:filename>", methods=['GET', 'POST'])
# def view(filename=None):


@app.route('/create-report/', methods=['GET', 'POST'])
def read_file():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if not allowed_file(file.filename):
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(filename)
        try:
            CreateReportFile(filename)
            # ToDO: delete the input file.
            return render_template('download.html')
        except Exception as e:
            return f"<p>{e}</p>"

    return render_template("home.html")


def run_application():
    """function that active the debugger and run the flask application"""
    port = int(os.environ.get("PORT", 8080))
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.debug = True
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    run_application()
