import streamlit as st

def render_map_page(conn):
    cursor = conn.cursor()
    st.header("충전소 현황")
    st.write("여기에 지도 들어갈 예정")
