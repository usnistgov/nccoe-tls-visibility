[[Name]] Server Configuration
-----------------------------

The [[Name]] server build started with a standard [[OS]] virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | [[NIC0]] | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | [[NIC1]] | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
ENUMERATE_Service_Version_Containerized


Notes
^^^^^

[[Description]]



The server was assigned the unique hostname [[Hostname]]. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The [[Name]] software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the [[Certificates]] directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, [[Name]] was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

ENUMERATE_Config

[[Configuration Description]]

Certificates location: ``[[Certificates]]``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the [[Name]] service was enabled through the following commands:

.. code-block:: bash

    [[Startup Instructions]]