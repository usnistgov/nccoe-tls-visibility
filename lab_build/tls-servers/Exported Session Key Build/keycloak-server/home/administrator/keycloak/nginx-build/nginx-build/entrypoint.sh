#!/bin/bash
  
cp /certs/DigiCertCAChain.crt.pem /etc/ssl/certs

adduser www-data eva-zone-1
#adduser root eva-zone-1
service syslog-ng start
service eva start

nginx -g "daemon off;"
