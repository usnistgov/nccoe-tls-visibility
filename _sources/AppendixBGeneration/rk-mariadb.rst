MariaDB Server Configuration
-----------------------------

The MariaDB server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.14  | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.24  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| MariaDB     | 11.0.2    | No            |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | No            |
+-------------+-----------+---------------+


Notes
^^^^^

As none of the currently available MariaDB container images on DockerHub used a version of OpenSSL supported by the Nubeva agent, the MariaDB 11.0.2 software was installed directly on the host VM.



The server was assigned the unique hostname rk-mariadb.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The MariaDB software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /etc/mysql/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, MariaDB was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration Files                                                                                                                                                                                                                           |
+===============================================================================================================================================================================================================================================+
| `/etc/mysql/mariadb.conf.d/50-server.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/mariadb-server/etc/mysql/mariadb.conf.d/50-server.cnf>`__ |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/mysql/mariadb.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/mariadb-server/etc/mysql/mariadb.cnf>`__                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/eva/eva-openssl.cnf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/mariadb-server/etc/eva/eva-openssl.cnf>`__                               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/etc/eva/eva.conf <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/tls-servers/Bounded-lifetime%20Rotated%20EDH%20Server%20Key%20Build/mariadb-server/etc/eva/eva.conf>`__                                             |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

MariaDB is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Key Management Agent receives key material through an SSH connection from the Key Governance Platform over the MANAGEMENT network, authenticated using an SSH key pair. MariaDB is secured with an SSL certificate issued through DigiCert. 

* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.


Certificates location: ``/etc/mysql/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the MariaDB service was enabled through the following commands:

.. code-block:: bash

    systemctl status enable mariadb