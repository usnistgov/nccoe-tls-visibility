NETSCOUT for Visibility Analytics
=============================

This section contains detailed instructions configuring the NetScout products used to perform real-time and post facto traffic analytics. These analytic capabilities are leveraged across all the real-time and post facto decryption previously described approaches. 

Instantiation of the NETSCOUT Virtual Appliances
------------------------------------------------

The NETSCOUT platform consists of four virtual appliances created from the vendor supplied OVF files: two vStream appliances, the ISNG appliance, and the OCI appliance. The vStream and vCyberStream appliances are provisioned with three network interfaces, and the ISNG and OCI appliances are each configured with a single network interface. 

The vStream appliance is used to provide decrypted and encrypted traffic to the NetScout ISNG appliance.

Similarly, the vCyberStream appliance is used to provide decrypted and encrypted traffic to the NetScout OCI appliance.


NetScout vStream Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+-----------------+--------------------------------------------------------------------------------+
| Interface | Network    | IP Address      | Purpose                                                                        |
+===========+============+=================+================================================================================+


NetScout vCyberStream Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+-----------------+--------------------------------------------------------------------------------+
| Interface | Network    | IP Address      | Purpose                                                                        |
+===========+============+=================+================================================================================+


NetScout ISNG Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------+
| Interface | Network    | IP Address     | Purpose                                    |
+===========+============+================+============================================+


NetScout OCI Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------+
| Interface | Network    | IP Address     | Purpose                                    |
+===========+============+================+============================================+


Real-time Analytics
-------------------
The passive real-time decryptors and the break and inspect middleboxes each forward decrypted TLSv1.3 traffic to the real-time analytics platform over an isolated and secured network channel labeled ``DECRYPTED``. The real-time analytics are then performed on these streams of decrypted traffic within a limited time of the decrypted traffic's receipt. The decrypted traffic is retained by the analytics platform only as necessary and only for a short period of time.

Post-Facto Analytics
--------------------

In each of the lab builds, encrypted traffic is intercepted and forwarded to the post facto analytics platform by a network tap on the ``SERVER`` network segment over the ``ENCRYPTED`` network segment. The post facto analytics platform is responsible for securely managing the captured traffic, including its eventual destruction. Real world implementations of these architectures would require network taps from all of the various physical and logical networks that make up the data center's logical data plane. For the middlebox builds, an additional network tap may be placed on the client-facing network segment. Alternatively, the middlebox may copy the incoming and outgoing encrypted traffic directly to the ``ENCRYPTED`` network.





Configuration Procedure
-----------------------

[[Configuration Procedure Summary]]




Additional Configuration Files
------------------------------

+------------------------------------------------------------------------------------+
| Relevant Configuration Files                                                       |
+====================================================================================+

[[Configuration Files Description]]

