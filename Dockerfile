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
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8080
CMD ["python","main.py"]

