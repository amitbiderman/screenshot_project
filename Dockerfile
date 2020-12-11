FROM ubuntu:18.04


RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y \
    && apt-get install -y wget \
    && apt-get install unzip

RUN apt-get install -yqq unzip

RUN pip3 install --upgrade pip

RUN wget  https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 

RUN apt install ./google-chrome-stable_current_amd64.deb -y


RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/87.0.4280.88/chromedriver_linux64.zip


RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

ENV DISPLAY=:99


ENV PATH="/app:${PATH}"


COPY . /app
WORKDIR /app


COPY ./requirements.txt ./

RUN pip3 install -r ./requirements.txt

ADD main.py /


ENTRYPOINT ["python3", "main.py"]

