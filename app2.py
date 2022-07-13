import streamlit as st
import altair as alt
import pandas as pd


st.title('Twitter分析アプリ')
st.write('''
# このアプリはTwitter APIを使った分析アプリです。\n
ユーザーのタイムラインを様々な角度から分析します。
''')

option=st.sidebar.selectbox(
    'オプション',
    ['API認証とデータ取得','データ分析']

)
