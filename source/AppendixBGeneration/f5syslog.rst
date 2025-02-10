F5-Syslog Server Configuration
-----------------------------

The F5-Syslog server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.10.151 | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Syslog-ng   | 3.25.1    | No            |
+-------------+-----------+---------------+
| f5forwarder | N/A       | No            |
+-------------+-----------+---------------+


Notes
^^^^^

This server hosts a syslog-ng service collecting logs from the F5 BIG-IP device. These logs contain keys to be used for decryption. This server also hosts a python script which continuously reads the logs for these keys, and uploads them to the Redis database for use by the decryptors.



The server was assigned the unique hostname f5-syslog.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The F5-Syslog software was installed using the native "apt" Ubuntu package installer, as well as a custom python script which receives and forwards keys from F5's syslog to the Redis server.




Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| /home/tlsadmin/redis-forwarder/f5-redis.py                                     |
+--------------------------------------------------------------------------------+
| /home/tlsadmin/redis-forwarder/key-remover.py                                  |
+--------------------------------------------------------------------------------+
| /etc/syslog-ng/syslog-ng.conf                                                  |
+--------------------------------------------------------------------------------+
| /etc/systemd/system/f5forwarder.service                                        |
+--------------------------------------------------------------------------------+

* ``f5-redis.py`` is the python script used to forward keys extracted from syslog (received from F5 BIG-IP) to the Redis server.
* ``f5forwarder.service`` is used to keep the f5-redis.py script running constantly, so as to not fall behind on logs.
* ``key-remover.py`` is simply a tool used to clear the Redis database of keys. While not part of the build, it is included here for convenience.

Certificates location: ``/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the F5-Syslog service was enabled through the following commands:

.. code-block:: bash

    service syslog-ng start

    service f5forwarder start