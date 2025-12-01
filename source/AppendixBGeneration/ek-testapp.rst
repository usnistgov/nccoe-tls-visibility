TestApp Server Configuration
-----------------------------

The TestApp server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.21  | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.51  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Nginx       | 1.18.0    | Yes           |
+-------------+-----------+---------------+
| TestApp     | N/A       | Yes           |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | Yes           |
+-------------+-----------+---------------+


Notes
^^^^^

The web application server consists of an Nginx reverse proxy in front of a Python Flask application running in a Docker container. Docker Community Edition was installed, and the default non-root user was added to the docker OS group.



The server was assigned the unique hostname ek-testapp.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The TestApp software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /home/administrator/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, TestApp was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration Files                                                                                                                                                                                                                                                                  |
+======================================================================================================================================================================================================================================================================================+
| `/home/administrator/testapp-stack/nginx-build/nfr/conf/eva-openssl.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/nfr/conf/eva-openssl.cnf>`__ |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-build/nfr/conf/eva.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/nfr/conf/eva.conf>`__               |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-build/Dockerfile <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/Dockerfile>`__                             |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-build/nfr/openssl.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/nfr/openssl.cnf>`__                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-build/nfr/syslog-eva.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/nfr/syslog-eva.conf>`__           |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-build/entrypoint.sh <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-build/entrypoint.sh>`__                       |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-default.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-default.conf>`__                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/docker-compose.yml <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/docker-compose.yml>`__                                     |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/testapp-build/testapp/testapp.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Exported%20Session%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/testapp/testapp.py>`__         |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Nginx is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Nginx reverse proxy is secured with an SSL certificate issued through DigiCert. The docker files are primarily for ensuring that the service is running and using the correct certificates.

* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.

The Nginx container manages access to a small python application which acts as a web server. The docker files are primarily for ensuring that the service is running.

Certificates location: ``/home/administrator/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the TestApp service was enabled through the following commands:

.. code-block:: bash

    docker compose up -d