from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Here, you can handle the submitted data (e.g., save it to a database or send an email)
    print(f"Form Submitted: Name={name}, Email={email}, Message={message}")  # Logs to the console
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
