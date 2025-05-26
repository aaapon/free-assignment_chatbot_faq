import pandas as pd
import streamlit as st
import logging 

# 1. エラーメッセージを整形して画面に表示するための関数
def build_error_message(message: str) -> str:
    """
    ユーザー向けに表示するエラーメッセージを装飾付きで整形します。
    """
    return f"❌ {message} ❌"

# 2. FAQデータをCSVから読み込む関数
def load_faq_data(file_path: str) -> pd.DataFrame:
    """
    指定したCSVファイルからFAQデータを読み込んでDataFrameで返します。
    """
    try:
        df = pd.read_csv(file_path, encoding="utf-8-sig")
        return df
    except Exception as e:
        st.error("FAQデータの読み込みに失敗しました。ファイルの場所や内容を確認してください。")
        raise e