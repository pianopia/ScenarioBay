import eel

# Eelの設定
eel.init('web')

# メインのアプリケーションロジック
if __name__ == '__main__':

    # Eelアプリの起動
    eel.start('index.html', size=(800, 600), port=8083)

