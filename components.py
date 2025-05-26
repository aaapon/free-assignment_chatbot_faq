# 画面表示に関する関数を定義するファイル

import streamlit as st
import config as ct
from datetime import datetime

def display_date():
    """現在の日付を中央に表示する"""
    today = datetime.today().strftime("%Y-%m-%d")
    st.markdown(f"<div style='text-align:center; color: gray;'>{today}</div>",
                unsafe_allow_html=True
    )

def display_header():
    """チャットボットのヘッダーを表示する"""
    st.markdown(
        f"""
        <div style='background-color:#004aad; padding: 10px; color: white; font-size: 20px; font-weight: bold; border-top-left-radius: 10px; border-top-right-radius: 10px;'>
        {ct.APP_NAME}
        </div>
        """,
        unsafe_allow_html=True
    )

def display_initial_ai_message():
    """初期のAIメッセージを表示する"""
    st.markdown(
        f"""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 10px; max-width: 80%; margin: 10px auto;'>
            {ct.APP_DESCRIPTION}
        </div>
        """,
        unsafe_allow_html=True
    )
def message_bot():
    """AIの吹き出し表示"""
    st.markdown(
        f"""
        <div style='display: flex; align-items: start; margin-bottom: 10px;'>
            <img src='{ct.BOT_ICON}' width='40' style='margin-right: 10px;' />
            <div style='background-color: #f0f0f0; padding: 10px; border-radius: 10px; max-width: 80%;'>
                {ct.APP_DESCRIPTION}
            </div>
        </div>
        """,
        unsafe_allow_html=True

    )

def message_user(text: str):
    """ユーザーの吹き出し表示"""
    st.markdown(
        f"""
        <div style='display: flex; justify-content: flex-end; margin-bottom: 10px;'>
            <div style='background-colr: #d2e3fc; padding: 10px; border-radius: 10px; max-width: 80%;'>
                {text}
            </div>
        </div>
        """,
        unsafe_allow_html=True

    )

def display_faq_buttons(faq_df):
    """よくある質問ボタンを表示し、クリックされた質問を返す"""
    selected_question = None    # クリックされた質問を保存する変数

    # 横並びではなく縦並びにしたいため、ボタンを1個ずつ表示
    for question in faq_df["question"]:
        if st.button(question):
            selected_question = question
            break
    return selected_question

def display_conversation_log():
    """会話ログを表示する"""
    if "conversation_log" not in st.session_state:
        st.session_state.conversation_log = []

    # 会話ログが空でない場合のみ表示
    if st.session_state.conversation_log:
        for log in st.session_state.conversation_log:
            role, content = log["role"], log["content"]
            if role == "user":
                message_user(content)
            elif role == "bot":
                message_bot(content)
    else:
        st.markdown("まだ会話がありません。質問をしてみてください。")