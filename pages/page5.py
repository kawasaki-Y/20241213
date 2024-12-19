import streamlit as st
import sqlite3
import pandas as pd
import os

# データ取得
def get_topics():
    conn = sqlite3.connect("business_topics.db")
    df = pd.read_sql_query("SELECT * FROM topics", conn)
    conn.close()
    return df

# SQLファイルのダウンロード準備
def export_sql_file():
    with open("business_topics.sql", "w") as f:
        conn = sqlite3.connect("business_topics.db")
        for line in conn.iterdump():
            f.write(f"{line}\n")
        conn.close()

# Streamlit アプリ
st.title("経営トピック データベース参照")
st.markdown("このページでは登録済みの経営トピックを閲覧およびSQLファイルとしてエクスポートできます。")

# データ参照セクション
st.header("🔍 登録済みトピック")
data = get_topics()
if not data.empty:
    st.dataframe(data)  # データをテーブル形式で表示
else:
    st.info("現在、登録されているトピックはありません。")

# SQLファイルダウンロードセクション
st.header("🔐 SQLファイルのエクスポート")
if st.button("SQLファイルをダウンロード"):
    export_sql_file()
    with open("business_topics.sql", "rb") as file:
        st.download_button(
            label="SQLファイルをダウンロード",
            data=file,
            file_name="business_topics.sql",
            mime="application/sql"
        )
    os.remove("business_topics.sql")
