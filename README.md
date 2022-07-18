# Deep_Fetch

**Deep_Fetch** is an AI based detector which will fetch the PII entities and image from any Government ID's and use it further processing

![Generic badge](https://img.shields.io/badge/AI-Advance-green.svg) ![Generic badge](https://img.shields.io/badge/Python-3.6|3.7-blue.svg) ![Generic badge](https://img.shields.io/badge/pip-v3-red.svg) ![Generic badge](https://img.shields.io/badge/paddleocr-python-latest.svg) ![Generic badge](https://img.shields.io/badge/flask-latest-green.svg) ![Generic badge](https://img.shields.io/badge/streamlite-latest-green.svg) ![Generic badge](https://img.shields.io/badge/opencv-python-latest.svg)![Generic badge](https://img.shields.io/badge/yolox-python-latest.svg)


<h2><img src="https://cdn2.iconfinder.com/data/icons/artificial-intelligence-6/64/ArtificialIntelligence9-512.png" alt="Brain+Machine" height="38" width="38"> Creators </h2>

### [Mohan Kumar](https://github.com/kkkumar2?tab=repositories)

### Sandeep Jena

### [Mohammed squaib](https://github.com/saquibquddus?tab=repositories)

### Dilpa

# About the project

## Deep_Fetch
**Deep_Fetch** is an AI based detector which will fetch the PII entities and image from any Government ID's and use it further processing

## YOLOX
``YOLOX`` is an anchor-free version of YOLO, with a simpler design but better performance! It aims to bridge the gap between research and industrial communities.

``YOLOX`` is used to crop the image from the government id and store it in the database


# Setup and Usage

Clone the repository using below command:
```bash
git clone https://github.com/kkkumar2/Deep_Fetch.git
```
create a conda or virtual env environment using below command:
```bash
conda create -n [env_name] python=3.7 or
virtualenv [env name] --python=python3.7
```

to activate the environment:
```bash
conda activate [env_name] or
source virtualenv/[env_name]/Scripts/activate
```

To install Locally and test the application

```bash
pip install -r STREAMLIT/requirement.txt
pip install -r requirement.txt
```
To run the ``FLASK`` application open anaconda prompt
```bash
python main.py
```
To run the ``STREAMLIT`` application open anaconda prompt
```bash
cd STREAMLIT 
streamlit run Streamlit.py

Open localhost:8501 and Upload the Image and make sure Flask application is up before uploading 
```

To test the Application using Docker

command to up the services
```bash
docker-compose up
```

command to down the services
```bash
docker-compose down
```

if making any changes and need to re build the image then you can
```bash
cd [folder name]
docker build -t [image name:tag name] .
```
