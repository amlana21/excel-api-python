FROM ubuntu:18.04
RUN apt-get update -y && apt-get install software-properties-common -y  && apt-get upgrade -y && apt-get install curl -y
RUN mkdir /home/pipinstall && mkdir /home/flaskapp
RUN cd home/pipinstall && apt install python3-pip -y
RUN pip3 install Flask
ENV FLASK_APP app
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
EXPOSE 5000
WORKDIR /home/flaskapp
COPY requirements.txt /home/flaskapp
RUN pip3 install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]