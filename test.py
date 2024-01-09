# 必要なモジュールを追加
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# ブラウザの起動時のオプション設定
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# ブラウザの起動
# 起動させるブラウザにより、webdriver.以降が異なる。
driver = webdriver.Chrome(options=chrome_options)

# URLバーにURLを流し込み
driver.get("https://www.google.co.jp/")

# 検索バーの名前(ウィジェット名前)からDOM内の機能を引きずり出す
serach = driver.find_element(By.NAME,"q")
# 検索バーに文字列を流し込む
serach.send_keys("hell world")

# 検索ボタンの名前(ウィジェット名前)からDOM内の機能を引きずり出す
serachButton = driver.find_element(By.NAME,"btnK")
# ボタンをクリックする。
# 実行環境で異なるらしく、windows環境だとこれが安定する。
driver.execute_script('arguments[0].click();', serachButton)
