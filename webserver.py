# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import sys
from flask import Flask, render_template, request

maintenanceMode = False

app = Flask(__name__, static_folder='static')


@app.before_request
def before_request_func():
    if request.endpoint != 'maintenance' and maintenanceMode is True:
        return render_template('maintenance.html'), 503


@app.route('/maintenance')
def maintenance():
    global maintenanceMode
    maintenanceMode = not maintenanceMode
    return "maintenance", 503


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/site1')
def site1():
    return render_template('html1.html')


@app.route('/site2')
def site2():
    return render_template('html2.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    try:
        app.run(port=int(sys.argv[1]))
    except:
        app.run(port=5000)
