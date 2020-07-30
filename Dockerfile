FROM python:3.7-buster

RUN apt update && \
  apt install -y --no-install-recommends \
  locales

RUN python3 -m pip install pip==19.3.1

RUN locale-gen ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LC_CTYPE ja_JP.UTF-8
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8

RUN mkdir -p /etc/sysconfig && \
  echo 'ZONE="Asia/Tokyo"' > /etc/sysconfig/clock && \
  rm -f /etc/localtime && \
  ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

COPY . /opt/course-registration-api

RUN cd /opt/course-registration-api && \
  pip3 install pipenv && \
  pipenv install --system --ignore-pipfile --deploy

WORKDIR /opt/course-registration-api

ENTRYPOINT ["uwsgi", "--ini", "configuration/uwsgi.ini"]
