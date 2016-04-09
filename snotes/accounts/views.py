
from flask import Blueprint, request, render_template
from flask.ext.login import login_required, login_user

from snotes.accounts.models import User
from .forms import LoginForm

bp = Blueprint("accounts", __name__)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username='ruanzhao').first()
        login_user(user)
        return "accounts/login:"

    login_form = LoginForm()
    return render_template("accounts/login.html", form=login_form)


@bp.route("/setting", methods=["GET"])
@login_required
def setting():
    return "setting"

