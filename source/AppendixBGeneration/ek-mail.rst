Mail Server Configuration
-----------------------------

The Mail server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.8   | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.21  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Postfix     | 3.4.13    | Yes           |
+-------------+-----------+---------------+
| Dovecot     | 1:2.3.7.2 | Yes           |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | Yes           |
+-------------+-----------+---------------+


Notes
^^^^^

The Mail application server consists of a Postfix service and Dovecot service providing SMTP and IMAP capabilities, running in a Docker container. Docker Community Edition was installed, and the default non-root user was added to the docker OS group.



The server was assigned the unique hostname ek-mail.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The Mail software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /home/tlsadmin/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, Mail was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| /home/tlsadmin/build-mail-container-image/nfr/conf/eva-openssl.cnf             |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/nfr/conf/eva.cnf                     |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/Dockerfile                           |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/nfr/openssl.cnf                      |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/nfr/syslog-eva.conf                  |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/entrypoint.sh                        |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/build-mail-container-image/testusers.txt                        |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/mnt_postfix/main.cf                                             |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/mnt_postfix/master.cf                                           |
+--------------------------------------------------------------------------------+

Postfix is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Postfix server is secured with an SSL certificate issued through DigiCert. The docker files are primarily for ensuring the service is running and using the correct certificates.

* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.

In addition to the configs listed, it was also necessary to create MX records in the DNS for each mail server present in the build, to ensure that the external mail server could communicate with them. In this case, the following was added to ``DNS Resolver > General Settings > Custom options ...`` in the PFSense firewall:

``local-data: "ek-mail.visibility.nccoe.org. IN MX 10 ek-mail.visibility.nccoe.org"``

Certificates location: ``/home/tlsadmin/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the Mail service was enabled through the following commands:

.. code-block:: bash

    docker compose up -d