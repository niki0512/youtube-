import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

st.title('streamlit 超入門')

st.write('INterractive Widgets')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander=st.beta_expander('問い合わす')
expander.write('問い合わせ内容を書く')


# text=st.text_input('あんな他の趣味は')

# 'あなたの好きな数字は' ,text ,'です'

# cond=st.slider('あなたの今の調子は',0,100,50)
# 'コンデション',cond



# if st.checkbox('show Image'):
#     img=Image.open('apr.jpg')
#     st.image(img, caption='sun', use_column_width=True)






