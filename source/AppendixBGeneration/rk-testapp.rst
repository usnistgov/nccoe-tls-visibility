TestApp Server Configuration
-----------------------------

The TestApp server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.13  | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.23  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Nginx       | 1.18.0    | No            |
+-------------+-----------+---------------+
| TestApp     | N/A       | Yes           |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | No            |
+-------------+-----------+---------------+


Notes
^^^^^

The web application server consists of an Nginx reverse proxy in front of a Python Flask application running in a Docker container. Docker Community Edition was installed, and the default non-root user was added to the docker OS group. Nginx was not containerized for this build to provide better compatibility with the SSH capability needed for key distribution.



The server was assigned the unique hostname rk-testapp.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The TestApp software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, TestApp was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration Files                                                                                                                                                                                                                                                                                                         |
+=============================================================================================================================================================================================================================================================================================================================+
| `/home/administrator/testapp-stack/testapp-build/testapp/oidc-client-secret.txt <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/testapp/oidc-client-secret.txt>`__ |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/testapp-build/testapp/testapp.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/testapp/testapp.py>`__                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/testapp-build/Dockerfile <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/Dockerfile>`__                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/testapp-build/pyvenv.cfg <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/pyvenv.cfg>`__                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/testapp-build/requirements.txt <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/testapp-build/requirements.txt>`__                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/docker-compose.yml <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/docker-compose.yml>`__                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/home/administrator/testapp-stack/nginx-default.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/home/administrator/testapp-stack/nginx-default.conf>`__                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/eva/eva-openssl.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/etc/eva/eva-openssl.cnf>`__                                                                                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/eva/eva.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/testapp-server/etc/eva/eva.conf>`__                                                                                                                           |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Nginx is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Key Management Agent receives key material through an SSH connection from the Key Governance Platform over the MANAGEMENT network, authenticated using an SSH key pair. The Nginx reverse proxy is secured with an SSL certificate issued through DigiCert. 


* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.

The Nginx container manages access to a small python application which acts as a web server. The docker files are primarily for ensuring that the service is running.

Certificates location: ``/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the TestApp service was enabled through the following commands:

.. code-block:: bash

    docker compose up -d

    service nginx start