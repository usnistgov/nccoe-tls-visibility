.. _f5-mb:

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

.. include:: AppendixBGeneration/f5syslog.rst






Configuration Procedure
-----------------------

This section describes the configuration of the F5 BIG-IP device for intercepting encrypted traffic on Layer 3 and outputting the decrypted traffic.

#. The following ``SSL Orchestrator`` policies were configured to support decryption, and associated with the profiles created. This will be highly dependent on the individual build. 

   .. figure:: /images/figures/f5-ssl-orchestrator.png
      :width: 90%
      :alt: Image showing SSL Orchestrator policies.

      SSL Orchestrator





#. Upload each certificate by navigating to ``System > Certificate Management > Import SSL Certificates and Keys``. Select ``Certificate`` for ``Import Type``.

   .. figure:: /images/figures/f5-upload-certificate.png
      :width: 90%
      :alt: Image showing certificate import.

      Import Certificates





#. Upload each key by navigating to ``System > Certificate Management > Import SSL Certificates and Keys``. Select ``Key`` for ``Import Type``.

   .. figure:: /images/figures/f5-upload-key.png
      :width: 90%
      :alt: Image showing key import.

      Import Keys





#. Create profiles for each server by navigating to ``System > Profiles > SSL``. ``force13_clientssl`` was used as the base profile, and the correct certificates are selected for ``Certificate Key Chain``.

   .. figure:: /images/figures/f5-profile.png
      :width: 90%
      :alt: Image showing profile creation.

      Profile Creation





#. For this setup, a pool was created for each server, to ensure that F5 BIG-IP acted as a reverse proxy, by navigating to ``Pools``.

   .. figure:: /images/figures/f5-pool.png
      :width: 90%
      :alt: Image showing pool settings.

      Pool Settings





#. A virtual server is created for each server by navigating to ``Virtual Server``.

   .. figure:: /images/figures/f5-virtual-server.png
      :width: 90%
      :alt: Image showing virtual server creation.

      Virtual Server Creation





#. Ensure that the correct ``SSL profile`` is associated with each virtual server. Note that ``Client`` refers to the F5 BIG-IP product acting as a client (communicating with the TLS servers), and ``Server`` refers to the product acting as a server (communicating with clients of the TLS servers).

   .. figure:: /images/figures/f5-virtual-server-settings.png
      :width: 90%
      :alt: Image showing virtual server settings.

      Virtual Server Settings





#. ``Address Translation`` and ``Port Translation`` are enabled, along with setting ``Source Address Translation`` to ``Auto Map`` in order to enable the reverse proxy to remap IP addresses from ``192.168.60.0/24`` to ``192.168.30.0/24``.

   .. figure:: /images/figures/f5-virtual-server-settings2.png
      :width: 90%
      :alt: Image showing virtual server address translation settings.

      Virtual Server Address Translation





#. It is important to ensure that the decryptor policies are selected under ``Access Policy``.

   .. figure:: /images/figures/f5-virtual-server-settings3.png
      :width: 90%
      :alt: Image showing Access Policy Settings.

      Virtual Server Access Policy








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

