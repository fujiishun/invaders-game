import pygame
import io
from PIL import Image
import threading

# Pygameの初期化
pygame.init()
screen = pygame.Surface((800, 600))  # メモリ上のSurfaceを使用

# Pygameの描画を画像に変換し、Flask経由で配信する関数
def generate_frame():
    while True:
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (255, 0, 0), (400, 300), 50)

        image = pygame.surfarray.array3d(screen)
        image = Image.fromarray(image.transpose((1, 0, 2)))

        with io.BytesIO() as output:
            image.save(output, format="JPEG")
            frame = output.getvalue()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Pygameのメインループを別スレッドで実行する関数
def run_pygame():
    threading.Thread(target=_pygame_loop).start()

def _pygame_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()
