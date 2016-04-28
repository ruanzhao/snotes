
from flask import Blueprint, request, render_template

from .forms import LoginForm
from .models import User

home = Blueprint('home', __name__)


@home.route('/')
def index():
    return render_template("home/index.html")


@home.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username='ruanzhao').first()
        login_user(user)
        return "accounts/login:"

    login_form = LoginForm()
    return render_template("home/login.html", form=login_form)


@home.route('/logout', methods=['GET', 'POST'])
def logout():
    return "logout"
