FROM python:3.8.13-slim-buster
RUN mkdir /opt/stream
WORKDIR  /opt/stream
COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .
EXPOSE 8501
CMD ["streamlit","run","Streamlit.py"]

#FROM ubuntu:14.04