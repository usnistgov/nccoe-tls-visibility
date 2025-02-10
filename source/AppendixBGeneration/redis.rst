Redis Server Configuration
-----------------------------

The Redis server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.10.150 | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Redis       | 7.2.4     | No            |
+-------------+-----------+---------------+


Notes
^^^^^

Redis 7.2.4 was built from source for this build, in order to enable the ability to use TLS when connecting to it. To do this, the following command was used:

``make BUILD_TLS=yes``


The server was assigned the unique hostname redis.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The Redis software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /home/administrator/redis-baremetal/redis-7.2.4/certs/ directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, Redis was configured to only listen on the network interface connected to the MANAGEMENT network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| redis.conf                                                                     |
+--------------------------------------------------------------------------------+

The primary usage of ``redis.conf`` was to ensure the ability to use TLSv1.3 and to indicate the certificates needed for the TLSv1.3 connection between it and the various products directly inserting keys into it.

Certificates location: ``/home/administrator/redis-baremetal/redis-7.2.4/certs/``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the Redis service was enabled through the following commands:

.. code-block:: bash

    service redis restart