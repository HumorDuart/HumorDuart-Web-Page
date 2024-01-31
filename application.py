from flask import Flask, render_template, send_from_directory, request


app = Flask(__name__, static_folder='static')
app.secret_key = b'\xf7\x81Q\x89}\x02\xff\x98<et^'



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images/logo'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route('/home.html')
@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/confirmar-subscripcio')
def confirmar_subscripcio():
    return render_template('confirmar-subscripcio.html')
    



# start the server
if __name__ == '__main__':
    app.run(debug=False)
