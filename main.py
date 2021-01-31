from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    # JSON.stringify; массив оъектов класса User
    participants = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    responsible_user = db.Column(db.String(100))  # id from User


class User(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    first_name = db.Column(db.String(100))
    second_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


class Task(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    fact_time = db.Column(db.Integer)
    price = db.Column(db.Float)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)  # JSON.stringify; массив оъектов класса User
    participants = db.Column(db.String(100))
    complete = db.Column(db.Boolean)
    responsible_user_id = db.Column(db.String(100))
    comments = db.Column(db.String(1000))  # JSON.stringify(comments_array)
    status = db.Column(db.String(100))  # open, close, work
    project_id = db.Column(db.String(100))


@app.route('/')
def home():
    token = request.headers.get('token')
    print(token)
    print(User.query.get(token))
    return jsonify({'success': True})


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
