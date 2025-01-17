FROM ubuntu:20.04

LABEL maintainer="NCCoE Administrator"
LABEL version="0.1"
LABEL description="This is custom Docker Image for an Nginx reverse proxy service."

ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y openssl=1.1.1f-1ubuntu2*
RUN apt-get install -q -y syslog-ng
RUN apt update && \
    apt install -y nginx && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean 

COPY ./nfr/eva.deb /tmp/nfr/eva.deb
RUN dpkg -i /tmp/nfr/eva.deb

COPY entrypoint.sh /tmp/entrypoint.sh
RUN chmod +x /tmp/entrypoint.sh

ENV nginx_vhost /etc/nginx/sites-available/default
ENV nginx_conf /etc/nginx/nginx.conf

#CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80 443
