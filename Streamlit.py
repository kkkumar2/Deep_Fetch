from engine import run
import streamlit as st
import os
import numpy as np
from PIL import Image
import pandas as pd

def save_uploaded_file(uploaded_file):
    try:
        os.makedirs('uploads',exist_ok=True)
        with open(os.path.join('uploads',uploaded_file.name),'wb') as f:
            f.write(uploaded_file.getbuffer())
        return 1,os.path.join('uploads',uploaded_file.name)
    except Exception as e:
        print(F"Error is {e}")
        return 0

app_mode = st.sidebar.selectbox('Application mode',
['About App','Upload image'])
if app_mode =='About App':
    with open("README.md", "r", encoding="utf-8") as fh:
        readme = ""
        unwanted_list = ['<h2>','![GIF]','## Dataset','<a href=','A demo']
        for line in fh:            
            if line.startswith(tuple(unwanted_list)): 
                continue
            readme = readme + line
    st.markdown(readme)

elif app_mode == "Upload image":
    # WINDOW = st.image([])  
    for i in os.listdir('uploads'):
        os.remove(os.path.join('uploads', i))
    uploaded_file = st.file_uploader(label="Upload an image", type=[ "jpg", "jpeg",'png'])
    if uploaded_file is not None:
        status,path = save_uploaded_file(uploaded_file)
        if status:
            image = np.array(Image.open(uploaded_file)) 
            st.image(image)
            # out = {"name":["mohankumar"],"DOB":["23/03/1997"]} ## used for testing purpose
            out = run(path)
            img = os.listdir("output")
            df = pd.DataFrame(out)
            st.dataframe(df)
            if len(image):
                st.image(Image.open(os.path.join('output',img[-1])),caption='Detect Image',width=100)
        else:
            print("File is not proper")
    
    