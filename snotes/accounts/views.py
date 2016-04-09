
from flask import Blueprint, request, render_template
from flask.ext.login import login_required, login_user

from snotes.accounts.models import User

bp = Blueprint("accounts", __name__)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username='ruanzhao').first()
        login_user(user)
        return "accounts/login:"
    
    return render_template("accounts/login.html")


@bp.route("/setting", methods=["GET"])
@login_required
def setting():
    return "setting"

