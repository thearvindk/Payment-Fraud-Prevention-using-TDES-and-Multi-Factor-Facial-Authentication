from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy

# import our model from folder
from face_recognition_and_liveness.face_liveness_detection.face_recognition_liveness_app import recognition_liveness

app = Flask(__name__)
app.secret_key = 'web_app_for_face_recognition_and_liveness' # something super secret
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Users(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    password = db.Column(db.String(100))

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session.pop('name', None)
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        print(user)
        if user is not None and user.password == password:
            session['name'] = user.name # store variable in session
            detected_name, label_name = recognition_liveness('face_recognition_and_liveness/face_liveness_detection/liveness.model',
                                                    'face_recognition_and_liveness/face_liveness_detection/label_encoder.pickle',
                                                    'face_recognition_and_liveness/face_liveness_detection/face_detector',
                                                    'face_recognition_and_liveness/face_recognition/encoded_faces.pickle',
                                                    confidence=0.5)
            if user.name == detected_name and label_name == 'real':
                return redirect(url_for('main'))
            else:
                return render_template('login_page.html', invalid_user=True, username=username)
        else:
            return render_template('login_page.html', incorrect=True)

    return render_template('login_page.html')

@app.route('/main')
def main():
    return redirect('http://localhost:5000/',code=302)

if __name__ == '__main__':
    db.create_all()

    # add users to database

    # new_user = Users(username='Vishvesh', password='1234', name='Vishvesh')
    # db.session.add(new_user)

    # new_user_2 = Users(username='earth_ekaphat', password='123456789', name='Ekaphat')
    # new_user_3 = Users(username='bonus_ekkawit', password='123456789', name='Ekkawit')
    # db.session.add(new_user_2)
    # db.session.add(new_user_3)

    app.run(host="localhost", port=8000, debug=True)