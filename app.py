import time
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

messages = [
    {
        'time': '11:22:03',
        'name': 'Guest',
        'content': 'hey everyone whats up'
    },
    {
        'time': '11:22:03',
        'name': 'dominos',
        'content': 'sup'
    },
]


@app.route('/')
def homepage():
    return render_template('index.html', messages=messages)


@app.route('/', methods=['POST'])
def post_comment():
    name = request.form['name'] or 'Guest'
    content = request.form['content']
    messages.append({
        'time': time.strftime('%X'),
        'name': name,
        'content': content,
    })
    return redirect('/')


@app.route('/login')
def login_page():
    message = request.args.get('message')
    return render_template('login.html', message=message)


@app.route('/login', methods=['POST'])
def process_login():
    return redirect('/login?message=Login failed!')


if __name__ == '__main__':
    app.run()
