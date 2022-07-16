FROM python:3.8.13-slim-buster
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 8501
CMD ["streamlit","run","Streamlit.py"]
