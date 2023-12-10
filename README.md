# Microorganism Detection in Water

## Background
**In the aqueous tapestry that sustains life, the role of environmental microorganisms (EMs) in water takes center stage, especially when it comes to the paramount concern of public health. Every drop of water tells a story, and within it, microscopic actors play a crucial part.**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Microorganism.gif)

- Detecting these environmental microorganisms is not just a scientific endeavor but a vital step in safeguarding communities against waterborne threats.
 - From identifying potential pathogens that could jeopardize public health to ensuring the purity of our drinking water sources, the microscopic world within water holds the answers.

## Dataset
The overall dataset is made up of the following two datasets:

- Environmental Microorganism Image Dataset Seventh Version is a microscopic image data set containing 41 types of EMs, with 2,65 images and 13,216 labeled objects in XML Format. 
- Environmental Microorganism Image Dataset Sixth Version is a microscopic image data set containing 21 types of EMs. Each type of EM contains 40 original and 40 GT images, in total 1680 EM ages.
- Box annotations were generated using the Roboflow tool, generating XML and YoloV8 files.
## Solution
**In this project we aim to develop application that can detect microorganisms and classifying water into contaminated and non-contaminated based on pathogen type.**

- Water Contamination Determination.
- Micoorganism Detection in Water.

| No | Description            | Dataset | Kaggle   | 
|:---| :--------------------- | :-----:  | :-----:  | 
|1| Water Contamination Determination | [Link](https://www.kaggle.com/datasets/saloni1712/emds7-1)|  [Link](https://www.kaggle.com/code/sudhanshu2198/microorganism-detection)        | 
|2| Microorganism Detection in Water | [Link](https://www.kaggle.com/datasets/saloni1712/emds7-1)|  [Link](https://www.kaggle.com/code/sudhanshu2198/drinking-water-contamination-determination)        |

## Project Links: 
1. [Streamlit Webapp](https://environmental-microorganism-detection.streamlit.app/)

## 🛠 Skills
Pytorch, Torchvision, Ultralytics, OpenCV, Numpy, Streamlit, Git

## Directory Tree
```bash

├── Srastog
│   ├── EfficientNet
│   │   ├── Accuracy_plot.PNG
│   │   ├── Classification_report.PNG
│   │   ├── Loss_plot.PNG
│   │   ├── efficientnet_weights
│   │   └── Water_contamination_EfficientNet.ipynb
│   ├── FasterRCNN
│   │   ├── inference.PNG
│   │   ├── inference_result.PNG
│   │   ├── map_table1.PNG
│   │   ├── map_table2
│   │   └── FasterRCNN_microorganism_detection.ipynb
│   ├── SSD
│   │   ├── inference.PNG
│   │   ├── inference_result.PNG
│   │   ├── map_table1.PNG
│   │   ├── map_table2
│   │   └── SSD_microorganism_detection.ipynb
├── images
│   ├── default_img
│   ├── Micro.PNG
│   ├── contamin.PNG
├── pages
│   ├── Microorganism_Detection.py
│   └── Water_Contamination.py
├── weights
│   ├── contamination.pth
│   └── microorganism_detection.pth
├── Introduction.py
├── README.md
├── requirements.txt
├── utils.py
└── .gitignore
```

## Water Contamination Determination

**Accuracy Plot**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/EfficientNet/Accuracy_plot.PNG)

**Loss Plot**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/EfficientNet/Loss_plot.PNG)

**Confusion Matrix**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/EfficientNet/Classification_report.PNG)

**Inference**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/images/contamin.PNG)

## Micoorganism Detection

**Metrics**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/FasterRCNN/inference_result.PNG)

**Map @ iou=0.50**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/FasterRCNN/map_table1.PNG)
![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/FasterRCNN/map_table2.PNG)

**Inference**

![](https://github.com/sudhanshu2198/Environmental-Microorganism-Detection/blob/master/Srastog/FasterRCNN/inference.PNG)

## Run Webapp Locally

Clone the project

```bash
  git clone https://github.com/sudhanshu2198/Environmental-Microorganism-Detection
```

Change to project directory

```bash
  cd Environmental-Microorganism-Detection
```
Create Virtaul Environment and install dependencies

```bash
  python -m venv venv
  venv/Scripts/activate
  pip install -r requirements.txt
```

Run Locally
```bash
  streamlit run Introduction.py
```
