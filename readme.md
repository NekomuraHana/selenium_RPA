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

linuxなら展開後のバイナリ本体を`/usr/local/bin/`へ入れる。

windowsならバイナリ本体をCドライブの任意フォルダへ入れて、PATHを通す

## 注意点
使用するwebドライバで挙動が変わる。
このサンプルはchrome向けにチューンされている。

## 行なっていること

行なっている手順としては次の通り

1. ブラウザの立ち上げ
2. URLの入力
3. googleの検索バーへ文字列を代入
4. 「検索ボタン」をクリック

## webページの操作の鍵となること

webページ内にあるウィジェット(部品)の名前等を事前に調べる必要がある。

調べ方は各webブラウザの開発モードにして、webページの構造を解析する。

## ファイル構成

- test.py : 実行プログラム本体
- requirements.txt : プログラムに必要なモジュール
- setupAndRun.ps1 : powerShell用の環境構築＆実行スクリプト
- .gitignore: gitで管理しないファイルとディレクトリの設定