import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np


root_dir=os.path.dirname(os.path.abspath(__file__))
homepage_img_dir=os.path.join(root_dir,"images","home_page")

st.title("Microorganism Detection in Water")
st.subheader("Project Description")
st.write("Environmental microorganisms (EMs) are ubiquitous around us and have an important impact on the survival\
         and development of human society. The detection of environmental microorganism indicators is essential for \
         for assessing the degree of pollution. Faster-RCNN, YOLOv3, SSD and RetinaNet object detection algorithm\
         are utilized are detecting microorganism in water...........")

st.subheader("Dataset")
st.write("The Environmental Microorganism Image Dataset Seventh Version is a microscopic image data set, including\
             the original Environmental Microorganism images (EMs) and the corresponding object labeling files in xml\
             format file. The EMDS-7 data set consists of 41 types of EMs, which has a total of 2365 images and 13216 \
             labeled objects...........")