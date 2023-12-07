import streamlit as st

title_cols = st.columns(3)
with title_cols[1]:
    title_writing = "Test Title"
    title_format = f'<p style="text-align: center; font-family: ' \
                   f'Arial; color: #808080; font-size: 40px; ' \
                   f'font-weight: bold;">{title_writing}</p>'
    st.markdown(title_format, unsafe_allow_html=True)
subtitle_cols = st.columns(3)
with subtitle_cols[1]:
    sub_title_writing = "Test Subtitle"
    subtitle_format = (
        f'<p style="text-align: center; font-family: Arial; '
        f'color: #808080; font-size: 32px; font-weight: bold;">'
        f'{sub_title_writing}</p>')
    st.markdown(subtitle_format, unsafe_allow_html=True)
