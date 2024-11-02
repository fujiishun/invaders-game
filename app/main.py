from app import create_app
from app.components.top import run_pygame

# Flaskアプリケーションを初期化
app = create_app()

if __name__ == "__main__":
    # Pygameを別スレッドで実行
    run_pygame()
    # Flaskアプリケーションを起動
    app.run(host="0.0.0.0", port=8000, debug=False)
