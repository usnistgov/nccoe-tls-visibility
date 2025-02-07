F5 BIG-IP as a Layer 3 Middlebox
=============================

This build uses the F5 BIG-IP product as a middlebox to actively break and inspect TLSv1.3 traffic. 

Instantiation of the F5 BIG-IP Virtual Appliance
-----------------------------------------------

The virtual appliance is instantiated from the vendor supplied virtual appliance template (OVF) file with four network interfaces configured as detailed below. Each network interface is assigned a static IP address on the appropriate subnet. The product instructions were followed for applying the appropriate license keys to the virtual appliance, creating the default administrative user, as well as adding and configuring the four network interfaces.

Additionally, a separate VM was created for the purpose of forwarding exported session keys to the Redis server used by AppViewX and other decryptors. This server runs a syslog server, and converts messages containing keys to the FastKey JSON file, which are then pushed into Redis for use by the decryptors.


F5 BIG-IP Active Decryptor Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | MANAGEMENT | 192.168.10.2           | Access to the web-based management console and connectivity to other products.                    |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 2         | SRVPATCHA1 | 192.168.60.2           | Upstream of Layer 3 F5 BIG-IP.                                                                    |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 3         | SRVPATCHA2 | 192.168.70.1           | Downstream of Layer 3 F5 BIG-IP.                                                                  |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 4         | DECRYPTED  | N/A Layer 2 connection | Access to the network where decryptors output the decrypted traffic.                              |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

Additional Modules
^^^^^^^^^^^^^^^^^^
The primary appliance was provisioned with the following modules from the ``System > Resource Provisioning`` menu item:

+----------------------------------------------------------+
| Plugin Name                                              |
+==========================================================+
| SSL Orchestrator                                         |
+----------------------------------------------------------+
| Access Policy                                            |
+----------------------------------------------------------+

F5 BIG-IP Syslog Server Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+----------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                              |
+===========+============+========================+======================================================================+

This VM, running Ubuntu 20.04.6 LTS was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

.. include:: f5syslog.rst






Configuration Procedure
-----------------------

This section describes the configuration of the F5 BIG-IP device for intercepting encrypted traffic on Layer 3 and outputting the decrypted traffic.




Additional Configuration Files
------------------------------

+-----------------------------------------------------------------+
| Relevant Configuration Files                                    |
+=================================================================+
| big-ip/irules/nccoeKeyExportToRedisClientSide_iRule.txt         |
+-----------------------------------------------------------------+
| big-ip/irules/nccoeKeyExportToRedisServerSide_iRule.txt         |
+-----------------------------------------------------------------+
| big-ip/irules/ssloS_NETSCOUT-port_remap.txt                     |
+-----------------------------------------------------------------+
| big-ip/irules/sslo_BreakInspect-gw_in_t.txt                     |
+-----------------------------------------------------------------+
| big-ip/irules/sslo_BreakInspect-lib.txt                         |
+-----------------------------------------------------------------+

A number of iRules were defined for this build within F5. 

* The iRules ``nccoeKeyExportToRedisClientSide`` and ``nccoeKeyExportToRedisServerSide`` exist to forward acquired session keys to Redis, for use by the other decryptors.

* The ``ssloS_NETSCOUT-port_remap`` iRule remaps traffic from HTTPS to HTTP to better enable the intrusion detection system.

* Finally, the last two ``sslo_BreakInspect-lib`` and ``sslo_BreakInspect-gw_in_t`` iRules are associated with hosts to instruct the F5 product to perform Break & Inspect on these hosts.

