FROM python:3.8

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG DEBUG=false

MAINTAINER <berserg2010@gmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN if getent passwd node; then userdel --force node; fi \
&& if getent passwd ${USER_ID}; then userdel --force ${USER_ID}; fi \
&& if getent group node; then groupdel node; fi \
&& if getent group ${GROUP_ID}; then groupdel ${GROUP_ID}; fi \
&& groupadd --gid ${GROUP_ID} node \
&& useradd --no-log-init --no-create-home --uid ${USER_ID} --gid ${GROUP_ID} node

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY --chown=${USER_ID}:${GROUP_ID} requirements.txt ./requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

USER node

COPY --chown=${USER_ID}:${GROUP_ID} . ./
