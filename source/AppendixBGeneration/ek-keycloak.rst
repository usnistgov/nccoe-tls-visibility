Keycloak Server Configuration
-----------------------------

The Keycloak server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.11  | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.11  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Nginx       | 1.18.0    | Yes           |
+-------------+-----------+---------------+
| Keycloak    | 20        | Yes           |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | Yes           |
+-------------+-----------+---------------+


Notes
^^^^^

The Keycloak application server runs within a Docker container, with an Nginx HTTP server acting as a reverse proxy. Docker Community Edition was installed, and the default non-root user was added to the docker OS group.



The server was assigned the unique hostname ek-keycloak.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The Keycloak software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /home/administrator/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, Keycloak was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| /home/administrator/keycloak/nginx-build/nfr/conf/eva-openssl.cnf              |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/nfr/conf/eva.cnf                      |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/Dockerfile                            |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/nfr/openssl.cnf                       |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/nfr/syslog-eva.conf                   |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/entrypoint.sh                         |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/default.conf                                      |
+--------------------------------------------------------------------------------+
| /home/administrator/keycloak/nginx-build/docker-compose.yaml                   |
+--------------------------------------------------------------------------------+

Nginx is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Nginx reverse proxy is secured with an SSL certificate issued through DigiCert. The docker files are primarily for ensuring that the service is running and using the correct certificates.

* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.

Once operational, Keycloak was configured with a new realm named "CORP". Within this realm, a user named "testuser" was provisioned. Additionally, an OpenID Connect Client entry was created to allow authentication for a simple Python test application, as described in the Web Application Server Configuration. The docker files are primarily for ensuring that the service is running.

Certificates location: ``/home/administrator/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the Keycloak service was enabled through the following commands:

.. code-block:: bash

    docker compose up -d