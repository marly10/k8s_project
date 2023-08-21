# base image
FROM python:3.9-alpine

# set working directory
WORKDIR /app

# copy source code to container
COPY . .

# install dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r req.txt

# install and configure the ELK stack components
RUN apk add --no-cache openjdk11-jre-headless
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.12.1-linux-x86_64.tar.gz
RUN tar -xzf elasticsearch-7.12.1-linux-x86_64.tar.gz
RUN rm elasticsearch-7.12.1-linux-x86_64.tar.gz
RUN mv elasticsearch-7.12.1 /usr/share/elasticsearch
RUN chown -R daemon:daemon /usr/share/elasticsearch
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-7.12.1-linux-x86_64.tar.gz
RUN tar -xzf logstash-7.12.1-linux-x86_64.tar.gz
RUN rm logstash-7.12.1-linux-x86_64.tar.gz
RUN mv logstash-7.12.1 /usr/share/logstash
RUN chown -R daemon:daemon /usr/share/logstash
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-7.12.1-linux-x86_64.tar.gz
RUN tar -xzf kibana-7.12.1-linux-x86_64.tar.gz
RUN rm kibana-7.12.1-linux-x86_64.tar.gz
RUN mv kibana-7.12.1-linux-x86_64 /usr/share/kibana
RUN chown -R daemon:daemon /usr/share/kibana

# expose ports
EXPOSE 5000 9200 9300 5601

# set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENV ES_HOME=/usr/share/elasticsearch
ENV LS_HOME=/usr/share/logstash
ENV KIBANA_HOME=/usr/share/kibana

# run the command to start the app and the ELK stack components
CMD ["sh", "-c", "elasticsearch & logstash & kibana & flask run --host=0.0.0.0"]

#docker tag flask-app ricky1101/my-flask-app:v1 
#docker push ricky1101/my-flask-app:v1
#docker build -t my-flask-app .
#docker run -p 5000:5000 -p 9200:9200 -p 9300:9300 -p 5601:5601 flask-app