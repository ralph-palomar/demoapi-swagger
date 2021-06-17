FROM python:3.8
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install connexion[swagger-ui]
RUN pip3 install flask-cors
COPY . .
EXPOSE 8080
CMD ["python3", "main.py"]