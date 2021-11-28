FROM python:3

WORKDIR /app

COPY requirements.txt ./

COPY app.py ./

RUN pip3 install -r requirements.txt 

CMD [ "python","app.py"]

EXPOSE 8000





