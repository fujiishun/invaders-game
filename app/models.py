from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyのインスタンスを作成
db = SQLAlchemy()

# ユーザーモデルの定義
class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
