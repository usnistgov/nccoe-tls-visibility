Instantiation of the Mira ETO Middlebox Appliance
-------------------------------------------------

The virtual appliance is instantiated from the same virtual appliance template (OVF) file used for the Mira ETO passive build with four network interfaces.     

MIRA ETO Middlebox Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App1Interface_App1Network_App1IP_App1Purpose


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

For OSI Layer 2 active break-and-inspect decryption, a MIRA ETO decryptor is configured as a bump-in-the-wire between the appliance's ``main0`` and ``main1`` interfaces. Depending on configuration, the decrypted traffic will be written to either ``app0``, ``app1`` or both. The decryptor is bi-directional, breaking and inspecting TLS connections originating from either side of the middlebox.


From the Server menu item on the web administration console, select the ``Settings > Network`` to configure the appliance network connections. In addition to a management connection, the ETO appliance defines six functional connections by default, named ``main0``, ``main1``, ``app0``, ``app1``, ``aux0``, and ``aux1``. This build only uses the ``main0``, ``main1``, and ``app0`` interfaces. 

Using the Ethernet MAC address listed for each interface on the web console, ensure the corresponding virtual NIC of the virtual appliance is connected to the appropriate virtual network. In this build, ``main0`` is connected to the ``SRVPATCHB1`` network (for connectivity to the ``CORPWAN`` network), ``main1`` is connected to the ``SRVPATCHB2`` (for connectivity to the ``SERVER`` network), and ``app0`` is connected to the ``DECRYPTED`` network.
