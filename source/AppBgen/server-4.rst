MariaDB Server Configuration
=============================

The MariaDB server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
---------------------

+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address       | Purpose                                                                                          |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.14 | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.24 | Connectivity from TLS clients.                                                                   |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+

Service Details
---------------
+-----------+------------+---------------------------+
| Service   | Version    | Containerized             | 
+-----------+------------+---------------------------+
| MariaDB   | 11.0.2     | No                        |
+-----------+------------+---------------------------+
| OpenSSL   | 1.1.1f     | No                        |
+-----------+------------+---------------------------+


Notes
-----

As none of the currently MariaDB container images on DockerHub used a version of OpenSSL supported by the Nubeva agent, the MariaDB 11.0.2 software was installed directly on the host VM.



The server was assigned the unique hostname rk-mariadb.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The MariaDB software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /etc/mariadb/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, MariaDB was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
-------------------

[[Configuration Files]]

The configuration file  [[config=/etc/mysql/mariadb.conf.d/50-server.cnf]] was edited to set the "bind" parameter in the "[mysqld]" section to the VM's IP address on the SERVER network. Next, the MariaDB was configured to use the TLS certificate and key, by adding the section titled "# * SSL/TLS" to [[config=/etc/mysql/mariadb.conf.d/50-server.cnf]].

All files named in the SSL section of the configuration file contain the PKI information (certificate chain, certificate, or key) encoded in PEM format. 

The ssl_ca configuration parameter must name the file containing the certificate chain for the Certificate Authority that issued the server's PKI certificate. 

The ssl_cert configuration parameter must name the file containing the server's PKI certificate. 

The ssl_key configuration parameter must name the file containing the private key for the server's PKI certificate. 

Additionally, the configuration option "require-secure-transport" must be set to "on" and the option "tls_version" must be set to "TLSv1.3" (capitalization important) to enable TLSv1.3 functionality on the server.

Startup Instructions
--------------------

Finally, the MariaDB service was enabled through the following commands:

.. code-block:: bash
    systemctl status enable mariadb