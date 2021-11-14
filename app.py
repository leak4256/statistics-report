from flask import Flask, request, render_template
from statistics import CreateReportHtml, CreateReportFile
import os

'''allocated flask object'''
app = Flask(__name__)


@app.route('/')
def load():
    """loud the form to fill the properties"""
    return render_template('home.html')


@app.route("/create-report/", methods=['POST', 'GET'])
def create_report():
    if request.form['srcname']:
        try:
            if request.form['destname']:
                CreateReportFile(request.form['srcname'], request.form['destname'])
                return f'<h1>The report created successfully in :{request.form["destname"]}</h1>'
            st = CreateReportHtml(request.form['srcname'])
            return f'<h1 align=center>Statistics Report</h1><p>{st}</p>'
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
