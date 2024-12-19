import streamlit as st
import sqlite3

# データベース接続とテーブル作成
def init_db():
    conn = sqlite3.connect("business_topics.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            date_added TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# データ登録
def add_topic(title, description):
    conn = sqlite3.connect("business_topics.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO topics (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    conn.close()

# Streamlit アプリ
st.title("経営トピック データベース登録")
st.markdown("このページでは新しい経営トピックをデータベースに登録できます。")

# データベース初期化
init_db()

# データ登録セクション
st.header("✨ データ登録")
with st.form("add_form"):
    title = st.text_input("トピックタイトル", placeholder="例: 新規市場参入戦略")
    description = st.text_area("トピック詳細", placeholder="例: 新市場参入の戦略案や課題を記載してください。")
    submitted = st.form_submit_button("登録")
    if submitted:
        if title and description:
            add_topic(title, description)
            st.success("トピックを登録しました！")
        else:
            st.error("全てのフィールドを入力してください！")
