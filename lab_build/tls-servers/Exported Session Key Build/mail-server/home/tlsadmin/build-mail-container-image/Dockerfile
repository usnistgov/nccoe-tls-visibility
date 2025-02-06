FROM ubuntu:20.04

LABEL maintainer="NCCoE Administrator"
LABEL version="1"
LABEL description="This is a custom Docker Image for running Postfix with TLS 1.3"

ARG DEBIAN_FRONTEND=noninteractive

RUN export SHELL=/bin/bash
RUN apt-get update
RUN apt-get install -q -y syslog-ng
#RUN sed -i 's/system()/system(exclude-kmsg(yes))/g' /etc/syslog-ng/syslog-ng.conf
RUN apt-get install -y openssl=1.1.1f-1ubuntu*
RUN apt-get install -y postfix=3.4.13-0ubuntu*
RUN apt-get install -y dovecot-imapd=1:2.3.7.2-1ubuntu*
# RUN ufw allow postfix
#RUN mkdir /etc/postfix/
RUN mkdir /etc/postfix/tls
RUN chmod -R 644 /etc/postfix/
RUN chmod -R 644 /etc/postfix/tls/

#EXPOSE 25
EXPOSE 587
EXPOSE 143
EXPOSE 993
RUN useradd test_user_1
RUN useradd test_user_2
RUN useradd test_user_3
RUN mkhomedir_helper test_user_1
RUN mkhomedir_helper test_user_2
RUN mkhomedir_helper test_user_3

COPY testusers.txt /tmp/testusers.txt
RUN chpasswd < /tmp/testusers.txt
RUN rm /tmp/testusers.txt

COPY ./nfr/eva.deb /tmp/nfr/eva.deb
RUN dpkg -i /tmp/nfr/eva.deb

COPY entrypoint.sh /tmp/entrypoint.sh	
RUN chmod +x /tmp/entrypoint.sh
#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]

