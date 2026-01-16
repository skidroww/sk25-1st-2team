import streamlit as st

def render_faq_page(conn):
    cursor = conn.cursor()
    st.header("faq ")
    st.write("여기에 faq 들어갈 예정")