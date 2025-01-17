FROM ubuntu:20.04

LABEL maintainer="NCCoE Administrator"
LABEL version="0.1"
LABEL description="This is custom Docker Image for an Nginx reverse proxy service."

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y nginx && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean 

ENV nginx_vhost /etc/nginx/sites-available/default
ENV nginx_conf /etc/nginx/nginx.conf

CMD ["nginx", "-g", "daemon off;"]

EXPOSE 80 443
