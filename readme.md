# googleの自動検索

## お膳立て
実行環境で使うwebブラウザ用のドライバをいれる(webDriver)

### Chromeの場合

chromeDeiverを入れる。
https://chromedriver.chromium.org/downloads

### Firefoxの場合

geckodriverを入れる。
https://github.com/mozilla/geckodriver/releases

### webドライバのインストール

linuxなら展開後のバイナリ本体を`/usr/local/bin/`へ入れる
windowsならバイナリ本体をCドライブの任意フォルダへ入れて、PATHを通す

## 注意点
使用するwebドライバで挙動が変わる。
このサンプルはchrome向けにチューンされている。
