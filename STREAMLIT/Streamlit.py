import streamlit as st
# from engine import run
import os
import numpy as np
from PIL import Image
import pandas as pd
import json


def flask_call(path):
    # url = os.getenv("URL",None)
    url = "http://localhost:8080/detect" # it used for without docker
    # url = "http://web:8080/detect" # if used docer  then uncomment this line the commet bellow line no 12

    if url is None:
        raise "Service URL is not present"
    import requests

    files = {'image': open(path, 'rb')}
    out = requests.post(url, files=files)
    print(out.content)
    print(json.loads(out.content))
    return json.loads(out.content)

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
    os.makedirs("uploads",exist_ok=True)
    for i in os.listdir('uploads'):
        os.remove(os.path.join('uploads', i))
    uploaded_file = st.file_uploader(label="Upload an image", type=[ "jpg", "jpeg",'png'])
    if uploaded_file is not None:
        status,path = save_uploaded_file(uploaded_file)
        if status:
            image = np.array(Image.open(uploaded_file)) 
            st.image(image)
            # out = {"name":["mohankumar"],"DOB":["23/03/1997"]} ## used for testing purpose
            # out = run(path)
            out= flask_call(path)
            
            df = pd.DataFrame(out[0])
            st.dataframe(df)
            # print(out[1][0])
            bbox = out[1]
            if len(bbox):
                img = image[bbox[1]:bbox[3],bbox[0]:bbox[2]]
                st.image(Image.fromarray(img),caption='Detect Image',width=100)
        else:
            print("File is not proper")
    

