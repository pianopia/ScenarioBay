# ScenarioBay
Simple Canvas Memo Apps


```shell
# ビルド
$ pyinstaller main.py --onefile --osx-bundle-identifie=jp.cloudfree.louddin.rtf --add-data "web:web" --noconsole -w -F

$ python -m nuitka --msvc=14.2 --lto=no --standalone --onefile --onefile-tempdir-spec=ssl_server_tempdir --plugin-enable=pylint-warnings --plugin-enable=tk-inter --windows-disable-console --windows-product-name=server --windows-file-description="local server" --windows-product-version=0.0.0.1 --windows-company-name="BooleanEffect" --windows-icon-from-ico=C:\sk.ico ssl_server.py
```
