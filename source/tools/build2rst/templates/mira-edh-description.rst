Instantiation of the MIRA ETO Virtual Appliance
-----------------------------------------------

The MIRA ETO virtual machine was created in vSphere from the vendor supplied appliance (OVF) file with three network interfaces. 

MIRA ETO Passive Decryptor Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App1Interface_App1Network_App1IP_App1Purpose


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

The first interface is configured to connect to the lab ``MANAGEMENT`` network and provides access to the MIRA ETO web-based management console. The second and third interfaces are configured to connect to the ``ENCRYPTED`` and ``DECRYPTED`` networks and act as the source of encrypted traffic and destination for the resulting decrypted traffic streams. The assignment of the ``ENCRYPTED`` and ``DECRYPTED`` network connections to NICs on the virtual appliance is sensitive to the configuration of the appliance.