from flask import Flask, render_template , send_from_directory


HtmlFiles = """
 <!DOCTYPE html>
<html>
<body>

<p><a href="http://127.0.0.1:5000/1">site1</a></p>
<br>
<p><a href="http://127.0.0.1:5000/2">site2</a></p>
<br>

</body>
</html> 


"""



app = Flask(__name__, static_folder='static')


with app.open_resource('static\css1.css') as f:
    css1 = f.read()

with app.open_resource('static\css2.css') as f:
    css2 = f.read()
filename = "css1.css"

@app.route('/')
def index():
    return HtmlFiles

@app.route('/1')
def index1():
    return render_template('html1.html')

@app.route('/html11')
def index11():
    return render_template('html11.html')

@app.route('/css1')
def send_file1():
    return app.send_static_file("css1.css")


@app.route('/2')
def index2():
    return render_template('html2.html')

@app.route('/html22')
def index22():
    return render_template('html22.html')


@app.route('/css2')
def send_file2():
    return app.send_static_file("css2.css")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404



if __name__ == '__main__':
    app.run(debug=True)