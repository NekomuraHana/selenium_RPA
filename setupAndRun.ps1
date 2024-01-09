echo "start"

# pythonの仮想環境を作成 
python -m venv env

# 作成した仮想環境に入る
.\env\Scripts\Activate.ps1

# モジュールのインストール
pip install -r .\requirements.txt

# プログラム実行
python test.py

# 仮想環境から抜ける
deactivate
echo "end"