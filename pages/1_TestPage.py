import streamlit as st

title_cols = st.columns(3)
with title_cols[1]:
    title_writing = "Test Title 2"
    title_format = f'<p style="text-align: center; font-family: ' \
                   f'Arial; color: #808080; font-size: 40px; ' \
                   f'font-weight: bold;">{title_writing}</p>'
    st.markdown(title_format, unsafe_allow_html=True)
