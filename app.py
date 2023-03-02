from flask import Flask, render_template, redirect, url_for, request
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, login_required, current_user
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_login import login_user
from flask_bootstrap import Bootstrap
from models import User, Role

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_pyfile('config.py')
app.template_folder = 'templates'

db = MongoEngine(app)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


class RegistrationForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8)])
    submit = SubmitField('Register')

    def validate(self):
        if not super(RegistrationForm, self).validate():
            return False

        user = User.objects(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already registered.')
            return False

        return True


class LoginForm(Form):
    email = StringField('Email', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

    def validate(self):
        if not super(LoginForm, self).validate():
            return False

        user = User.objects(email=self.email.data).first()
        if not user or not user.check_password(self.password.data):
            self.email.errors.append('Invalid email or password')
            return False

        return True


@app.route('/', methods=['GET'])
@login_required
def home():
    return render_template('bootstrap/home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user_datastore.create_user(email=email, password=password)
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        user = User.objects(email=email).first()
        login_user(user)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('home'))

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
