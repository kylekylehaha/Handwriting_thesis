import time
import streamlit as st
import datetime
from PIL import Image
import numpy as np
import pandas as pd

# logo = Image.open('logo.png')


st.set_page_config(
    page_title="MAKE Lab Handwriting Performance APP",
    page_icon=Image.open('logo.png'),
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        "About":"# This is a header. This is an *extremely* cool app!"
    }
)

st.title('MAKE Lab Handwriting Performance APP')



st.markdown("## Introduction")
st.markdown('Our Task is try to upgrade sentence. Base on CEFR, we can choose which type you want to upgrade.')
st.markdown('For Example,  input sentence: **An big accident.**')
st.markdown('Then, we try to upgrade adjective. (i.e. In this sentence, we\' re going to upgrade  "big\") ')
st.markdown("Output: **An serious accident**")
st.markdown("Output: **An serious accident**")
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
    user_ASD = st.selectbox("實驗者是否患有自閉症?", ['是', '無'])
    user_ASD_

    submit_button = st.form_submit_button(label='填寫完成')

if submit_button:
    st.write('user name:', user_name)
# st.write('Upgrade type:', select)
    
with st.spinner(text='In progress'):
    for i in range(100):
        # Process language model
        time.sleep(0.1)
    st.success('Done')

# output result
