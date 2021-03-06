FROM python:3.8.13-slim-buster
# RUN mkdir /opt/fast
# WORKDIR  /opt/fast
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# https://stackoverflow.com/questions/29732990/installing-a-gcc-compiler-onto-a-docker-container
RUN apt-get update && \
    apt-get -y install gcc mono-mcs && \
    rm -rf /var/lib/apt/lists/*

RUN pip install cmake
# RUN pip install opencv-contrib-python
# RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get update && apt-get install libgl1 -y
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD ["python","main.py"]
