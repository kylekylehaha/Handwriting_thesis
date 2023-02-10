import time
import streamlit as st
import datetime
from PIL import Image
import numpy as np
import pandas as pd

# logo = Image.open('logo.png')


st.set_page_config(
    page_title="MAKE Lab Handwriting Performance APP",
    # page_icon=Image.open('logo.png'),
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About":"# This is a header. This is an *extremely* cool app!"
    }
)

st.title('MAKE Lab Handwriting Performance APP')



st.markdown("## Introduction")
# txt = st.text_area('Text to analyze', '''
#     It was the best of times, it was the worst of times, it was
#     the age of wisdom, it was the age of foolishness, it was
#     the epoch of belief, it was the epoch of incredulity, it
#     was the season of Light, it was the season of Darkness, it
#     was the spring of hope, it was the winter of despair, (...)
#     ''')
st.markdown('我們正在進行「**以口語表達與手寫表現探討自閉症兒童對於行為特徵與學習輔助**」之計畫。')
st.markdown('我們發現自閉症兒童和一般兒童在手寫表現上，有明顯的落差。（附圖一）')
st.markdown('因此，我們希望透過 AI 來分析兩者的筆跡，找出自閉症兒童特有的手寫特徵。')
st.markdown("最後，我們將透過訓練好的 AI，來開發出一款**藉由筆跡來分析手寫能力**的APP")
st.markdown("---")

st.markdown("## How to Use?")
st.markdown("### 第一步，填寫基本資料")

with st.form(key='User information'):
    user_name = st.text_input(label='你的名字')
    user_email = st.text_input(label="您的信箱")
    user_d = st.date_input("您的生日",datetime.date.today())
    user_gender = st.selectbox("性別", ["男性", "女性"])   # return type: list
    user_relation = st.selectbox("您和實驗者的關係", ['實驗者本人', '母親', '父親'])
    user_education = st.selectbox("教育程度", ['小學', '中學', '高中、高職', '大學', '碩士', '博士'])
    user_occupation = st.text_input(label='您的職業')
    user_handed = st.selectbox("寫字慣用手", ['右手', '左手'])
    user_independent = st.selectbox("生字本/作業本 是否獨立完成(例:家長扶著手幫忙寫)", ['是', '否'])
    user_ASD = st.selectbox("實驗者是否患有自閉症?", ['是，輕度', '是，中度', '是，重度', '無'])

    submit_button = st.form_submit_button(label='填寫完成')

if submit_button:
    st.write('user name:', user_name)
    st.write('user email:', user_name)
# st.write('Upgrade type:', select)
    with st.spinner(text='正在分析您的筆跡'):
        for i in range(100):
            # Process language model
            time.sleep(0.1)
    st.success('Done')
    


# output result
