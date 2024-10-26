from flask import Flask
from .models import db
from .routes import top, video_feed

def create_app():
    app = Flask(__name__)

    # データベースの設定
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:password@db:5432/invaders_db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # SQLAlchemyを初期化
    db.init_app(app)

    # ルートの登録
    app.register_blueprint(top)
    app.register_blueprint(video_feed)

    # コンテキスト内でテーブルを作成
    with app.app_context():
        db.create_all()

    return app
