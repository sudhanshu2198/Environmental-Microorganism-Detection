import streamlit as st
from PIL import Image
import cv2
import numpy as np
import os
import torch
import torchvision
from utils import classify_img,get_contamination_model

st.title("Water Contaminated Determination")
classes=["Not-Contaminated","Contaminated"]

model=get_contamination_model()
model.eval()
dirname=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.join(dirname,os.pardir)
classification_img_dir=os.path.join(root_dir,"images","default_img")

file=st.file_uploader("Input Image File",type = ['jpg','png','jpeg'])
button=st.button("Detect")
if button:
    if file is not None:
        title="Uploaded Image"
        img=Image.open(file)
        img=np.array(img)
        img=cv2.resize(img,(600,800))
        label,probability=classify_img(model,img)
    else:
        title="Default Image"
        idx=np.random.choice(range(15),1)[0]
        default_img_path=os.path.join(classification_img_dir,f"{idx}.png")
        img=Image.open(default_img_path)
        img=np.array(img)
        img=cv2.resize(img,(600,800))
        label,probability=classify_img(model,img)
    if label==0:
        st.success(f"Predicted Class is {classes[label]} with probability {probability:.4f}")
    else:
        st.error(f"Predicted Class is {classes[label]} with probability {probability:.4f}")
    img=cv2.resize(img,(480,480))
    st.image(img)
