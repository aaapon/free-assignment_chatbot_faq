import openai # OpenAIのAPIを使用するためのライブラリ
import logging # ログ出力のためのライブラリ
from config import MODEL_NAME, MODEL_TEMPERATURE # モデル名とランダムさをインポート
from initialize import load_dotenv # 環境変数を読み込む関数をインポート
import config as ct
import utils
import pandas as pd


# 1. 環境変数からAPIキーを読み込む(initialize.pyで定義された関数)
openai.api_key = load_dotenv()

# 2. ユーザーからの質問に対して、OpenAIのAPIを使って回答を生成する関数
def get_response_from_openai(user_message):
    try:
        # メッセージをchat形式で構築
        messages = [
            {"role": "system", "content": "あなたはカスタマーサポートのAIチャットボットです。"},
            {"role": "user", "content": user_message}
        ]
        # ChatGPTにリクエスト
        response = openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=MODEL_TEMPERATURE
)
        # 回答テキストを取り出す
        answer = response.choices[0].message["content"]

        # ログに記録(ユーザーの質問とAIの回答)
        logging.info(f"User: {user_message}")
        logging.info(f"AI: {answer}")
        return answer
    
    except Exception as  e:
        logging.error(f"エラー発生: {e}")
        return "申し訳ありません。エラーが発生しました。もう一度お試しください。"
        