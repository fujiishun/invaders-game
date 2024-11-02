from app import create_app
from app.models import db, User

# Flaskアプリケーションを初期化
app = create_app()

# シードデータの挿入
def insert_seed_data():
    with app.app_context():
        # ユーザーが存在しない場合のみシードデータを挿入
        if User.query.count() == 0:
            users = [
                User(name="yamada", email="yamada@example.com"),
                User(name="satou", email="satou@example.com"),
                User(name="tanaka", email="tanaka@example.com"),
            ]
            db.session.bulk_save_objects(users)
            db.session.commit()
            print("Seed data inserted successfully.")
        else:
            print("Seed data already exists.")

if __name__ == "__main__":
    insert_seed_data()
