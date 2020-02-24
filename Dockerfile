FROM python:3.8
RUN pip install -r requirements.txt
RUN python3 app.py --port 5000

EXPOSE 5000