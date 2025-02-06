MIRA ETO for Real-time Decryption using Exported Session Keys
=============================

This build uses the MIRA ETO product to passively decrypt TLSv1.3 network traffic leveraging exported TLS session keys. The MIRA ETO product is shared with the EDH keys build, and so the initial configuration and network setup is the same. However, the configuration is slightly different.

Instantiation of the MIRA ETO Virtual Appliance
-----------------------------------------------

The MIRA ETO virtual machine was created in vSphere from the vendor supplied appliance (OVF) file with three network interfaces. 

MIRA ETO Passive Decryptor Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+-----------------+--------------------------------------------------------------------------------+
| Interface | Network    | IP Address      | Purpose                                                                        |
+===========+============+=================+================================================================================+


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

The first interface is configured to connect to the lab ``MANAGEMENT`` network and provides access to the MIRA ETO web-based management console. The second and third interfaces are configured to connect to the ``ENCRYPTED`` and ``DECRYPTED`` networks and act as the source of encrypted traffic and destination for the resulting decrypted traffic streams. The assignment of the ``ENCRYPTED`` and ``DECRYPTED`` network connections to NICs on the virtual appliance is sensitive to the configuration of the appliance.





Configuration Procedure
-----------------------

This section describes the configuration of the MIRA ETO passive device to receive Exported Session Keys from the NFR EVA agents on the individual TLSv1.3 servers. In this build, this was configured using a separate server segment, and so this section will simply explain how to enable that segment. In practice it would be possible to perform both of these types of decryptions on the same segment.




Additional Configuration Files
------------------------------

+------------------------------------------------------------------------------------+
| Relevant Configuration Files                                                       |
+====================================================================================+

[[Configuration Files Description]]

