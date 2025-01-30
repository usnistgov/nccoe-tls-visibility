Keycloak Server Configuration
=============================

The Keycloak server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
---------------------

+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address       | Purpose                                                                                          |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.11 | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.11 | Connectivity from TLS clients.                                                                   |
+-----------+------------+---------------+--------------------------------------------------------------------------------------------------+

Service Details
---------------
+-----------+------------+---------------------------+
| Service   | Version    | Containerized             | 
+-----------+------------+---------------------------+
| Nginx     | 1.18.0     | Yes                       |
+-----------+------------+---------------------------+
| Keycloak  | 20         | Yes                       |
+-----------+------------+---------------------------+
| OpenSSL   | 1.1.1f     | Yes                       |
+-----------+------------+---------------------------+


Notes
-----

Insert Description



The server was assigned the unique hostname ek-keycloak.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The Keycloak software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the [[Certificates]] directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, Keycloak was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
-------------------

[[Configuration Files]]

Insert Description

Startup Instructions
--------------------

Finally, the Keycloak service was enabled through the following commands:

.. code-block::
    [[Startup Instructions]]