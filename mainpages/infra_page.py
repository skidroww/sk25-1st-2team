import streamlit as st

def render_infra_page(conn):
    cursor = conn.cursor()
    st.header("인프라 현황")
    st.write("여기에 인프라 들어갈 예정")