# Invaders Game - Docker で Pygame 環境構築

このプロジェクトは、Python と Pygame を使用して構築したシンプルなインベーダーゲームです。Windows 環境で Docker と X サーバー（VcXsrv）を使用して実行する手順を説明します。

## 事前準備

Docker Desktop および X サーバーのインストールが必要です。

DockerDesktop のダウンロードページ：https://www.docker.com/ja-jp/products/docker-desktop/
VcXsrv のダウンロードページ：https://sourceforge.net/projects/vcxsrv/

- VcXsrv をインストール後、スタートメニューから「XLaunch」を選択して起動します。
- Display settings：Multiple windows を選択し、Next をクリック。
- Client startup：Start no client を選択し、Next をクリック。
- Extra settings：Disable access control にチェックを入れ、Next をクリック。

## 起動手順

### リポジトリのクローン

以下のコマンドでリポジトリをクローンし、プロジェクトフォルダに移動します。

```
git clone https://github.com/fujiishun/invaders-game.git
cd invaders-game

```

### アプリの起動

```
docker-compose up --build -d

```

※コンテナ起動後、ブラウザで http://localhost:8000 へアクセス

### seed データ挿入

```
docker-compose exec game python app/seed.py

```
