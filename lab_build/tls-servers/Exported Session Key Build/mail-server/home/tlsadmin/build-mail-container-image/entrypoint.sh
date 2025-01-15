#!/bin/bash

VAR1="myhostname ="
VAR3=$(hostname | tr -d '\r')
VAR2="$VAR1$VAR3"
#sed -i -r "s/myhostname =/$VAR2/" "/etc/postfix/main.cf"
service syslog-ng start
echo "127.0.0.1 tlsv-lab $VAR3" >> /etc/hosts


#### EVA
cp /certs/DigiCertCAChain.crt.pem /etc/ssl/certs

adduser www-data eva-zone-1
adduser root eva-zone-1
service eva start
#### EVA


service dovecot start
postfix start-fg
