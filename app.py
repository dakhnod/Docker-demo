import flask
import mysql.connector as sql

app = flask.Flask(__name__)
connector = sql.connect(
    # host='172.17.0.2',
    port=3307,
    user='luga',
    password='luga',
    database='luga'
)

messages_db = [
    'First message'
]

def get_messages():
    cursor = connector.cursor()
    cursor.execute('SELECT message FROM messages')
    messages = cursor.fetchall()
    return [message[0] for message in messages][::-1]

@app.get('/')
def route_default():
    return flask.redirect('/messages')

@app.get('/messages')
def messages_display():
    return flask.render_template('messages.jinja2', messages=get_messages())

def insert_message(message):
    cursor = connector.cursor()
    cursor.execute('INSERT INTO messages (message) VALUES (%s)', (message,))
    connector.commit()

@app.post('/post')
def message_create():
    message = flask.request.form['message'][:64]
    insert_message(message)

    return flask.redirect('/messages')