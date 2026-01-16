import streamlit as st

def render_keyword_page(conn):
    cursor = conn.cursor()
    st.header("키워드 현황")
    st.write("여기에 키워드 들어갈 예정")