.. _mira-mb:

This build uses the MIRA ETO product as a middlebox to actively break and inspect TLSv1.3 traffic. Because of differences in networking requirements, the passive decryption instance of ETO could not be used for middlebox functionality. A separate instance of ETO was created to function as a middlebox. 

Instantiation of the Mira ETO Middlebox Appliance
-------------------------------------------------

The virtual appliance is instantiated from the same virtual appliance template (OVF) file used for the Mira ETO passive build with four network interfaces.     

MIRA ETO Middlebox Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | MANAGEMENT | 192.168.10.65          | Access to the web-based management console and connectivity to other products.                    |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 2         | SRVPATCHB1 | N/A Layer 2 connection | In combination with SRVPATCHB2, allows MIRA to act as a layer2 passthrough and intercept traffic. |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 3         | SRVPATCHB2 | N/A Layer 2 connection | In combination with SRVPATCHB1, allows MIRA to act as a layer2 passthrough and intercept traffic. |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 4         | DECRYPTED  | N/A Layer 2 connection | Access to the network where decryptors output the decrypted traffic.                              |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

For OSI Layer 2 active break-and-inspect decryption, a MIRA ETO decryptor is configured as a bump-in-the-wire between the appliance's ``main0`` and ``main1`` interfaces. Depending on configuration, the decrypted traffic will be written to either ``app0``, ``app1`` or both. The decryptor is bi-directional, breaking and inspecting TLS connections originating from either side of the middlebox.


From the Server menu item on the web administration console, select the ``Settings > Network`` to configure the appliance network connections. In addition to a management connection, the ETO appliance defines six functional connections by default, named ``main0``, ``main1``, ``app0``, ``app1``, ``aux0``, and ``aux1``. This build only uses the ``main0``, ``main1``, and ``app0`` interfaces. 

Using the Ethernet MAC address listed for each interface on the web console, ensure the corresponding virtual NIC of the virtual appliance is connected to the appropriate virtual network. In this build, ``main0`` is connected to the ``SRVPATCHB1`` network (for connectivity to the ``CORPWAN`` network), ``main1`` is connected to the ``SRVPATCHB2`` (for connectivity to the ``SERVER`` network), and ``app0`` is connected to the ``DECRYPTED`` network.






Configuration Procedure
-----------------------

This section describes the configuration of the MIRA ETO device for intercepting encrypted traffic on Layer 2 and outputting the decrypted traffic.




Additional Configuration Files
------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Relevant Configuration Files                                                                                                                              |
+===========================================================================================================================================================+
| `root/keylog2redis.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/mira-active-decryptor/root/keylog2redis.py>`__               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `root/keylog2redis.sh <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/mira-active-decryptor/root/keylog2redis.sh>`__               |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| `root/ScriptInstructions.txt <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/mira-active-decryptor/root/ScriptInstructions.txt>`__ |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

* The shell script ``keylog2redis.sh`` is used to run and capture the output of ``keylog2redis.py``.

* The python script ``keylog2redis.py`` is used to process Mira's log files for captured keys, and forward those keys to redis for use by the decryptors. 

