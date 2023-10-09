import streamlit as st
from PIL import Image
import cv2
import numpy as np
import tempfile
import torch
import os
import time
import torchvision
import torchvision.transforms.functional as tf
from utils import get_detection_model,detection_img


st.title("Microorganism Object Detection")

classes=['background','G001','G002','G003','G004','G005','G006','G007','G008',
         'G009','G010','G011','G012','G013','G014','G015','G016','G017','G018',
         'G019','G020','G021','G022','G023','G024','G025','G026','G027','G028',
         'G029','G030','G031','G032','G033','G034','G035','G036','G037','G038',
         'G039','G040','G041']
dirname=os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.join(dirname,os.pardir)
detection_img_dir=os.path.join(root_dir,"images","default_img")

model=get_detection_model()
model.eval()

file=st.file_uploader("Input Image File",type = ['jpg','png','jpeg'])
c1,c2=st.columns(2)
with c1:
    conf_threshold=float(st.slider("Confidence Threshold", min_value=0.0,max_value=1.0,value=0.3,step=0.02))
with c2:
    iou_threshold=float(st.slider("IOU Threshold", min_value=0.0,max_value=1.0,value=0.7,step=0.02))
col1,col2=st.columns(2)
button=st.button("Detect")
if button:
    if file is not None:
        title="Uploaded Image"
        img=Image.open(file)
        img=np.array(img)
        img=cv2.resize(img,(750,1000))
    else:
        title="Default Image"
        idx=np.random.choice(range(15),1)[0]
        default_img_path=os.path.join(detection_img_dir,f"{idx}.png")
        img=Image.open(default_img_path)
        img=np.array(img)
        img=cv2.resize(img,(750,1000))
    with col1:
        st.write(title)
        st.image(img)
    with col2:
        st.write("Microorganism Detection")
        detect_img=detection_img(model,img,classes,conf_threshold,iou_threshold)
        st.image(detect_img)
