# base image
FROM python:3.9-alpine

# set working directory
WORKDIR /app

# copy source code to container
COPY . .

# install dependencies
RUN pip install --no-cache-dir -r req.txt

# expose port
EXPOSE 5000

# set environment variables
ENV FLASK_APP=main.py
ENV FLASK_ENV=development

# run the command to start the app
CMD ["flask", "run", "--host=0.0.0.0"]

#docker tag flask-app ricky1101/my-flask-app:v1 
#docker push ricky1101/my-flask-app:v1