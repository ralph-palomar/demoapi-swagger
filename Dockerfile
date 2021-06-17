FROM python:latest
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install connexion[swagger-ui]
RUN pip3 install flask-cors
COPY . /usr/src/app
EXPOSE 8080
ENTRYPOINT ["waitress-serve"]
CMD ["--port=8080", "main:api"]