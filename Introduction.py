import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np


root_dir=os.path.dirname(os.path.abspath(__file__))
img_pth=os.path.join(root_dir,"images","Micro.PNG")
img=Image.open(img_pth)

st.title("Microorganism Detection in Water")
st.subheader("Project Description")
st.image(img)
st.write("In the aqueous tapestry that sustains life, the role of environmental microorganisms (EMs) in water takes \
          center stage, especially when it comes to the paramount concern of public health. Every drop of water tells a \
          story, and within it, microscopic actors play a crucial part. Detecting these environmental microorganisms is \
          not just a scientific endeavor but a vital step in safeguarding communities against waterborne threats. From \
          identifying potential pathogens that could jeopardize public health to ensuring the purity of our drinking water sources, \
          the microscopic world within water holds the answers. By delving into the unseen realms, we equip ourselves with the \
          knowledge needed to protect the most fundamental resource we all share—clean and safe water for the well-being of everyone.\
          The detection of environmental microorganism indicators is essential for assessing the degree of pollution. Faster-RCNN, \
          YOLOv3, SSD and RetinaNet object detection algorithm are utilized are detecting microorganism in water. ")

st.subheader("Dataset")
st.write("The overall dataset is made up of the following two datasets:")
st.markdown("""
            - Environmental Microorganism Image Dataset Seventh Version is a microscopic image data set containing 41 types of EMs, with 2,65 \
            images and 13,216 labeled objects in XML Format.
            - Environmental Microorganism Image Dataset Sixth Version is a microscopic image data set containing 21 types of EMs. Each type of EM \
            contains 40 original and 40 GT images, in total 1680 EM ages. Box annotations were generated using the Roboflow tool, generating XML and YoloV8 files.""")
