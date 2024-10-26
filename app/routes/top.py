from flask import Blueprint, render_template
from ..models import User

top = Blueprint("top", __name__)

@top.route("/")
def index():
    # usersテーブルから全ユーザーを取得
    users = User.query.all()
    return render_template("top/index.html", users=users)