from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "88e9e4104fde9819cabd352f8ea7974a'"


@app.route('/hello')
def index():
    return render_template('index.html')


@app.route('/greet', methods=['POST', 'GET'])
def greet():
    # line 16 of index.html
    flash(f'Hi {str(request.form["name_input"])}, great to see you!')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
