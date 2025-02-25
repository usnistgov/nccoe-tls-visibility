Instantiation of the F5 BIG-IP Virtual Appliance
-----------------------------------------------

The virtual appliance is instantiated from the vendor supplied virtual appliance template (OVF) file with four network interfaces configured as detailed below. Each network interface is assigned a static IP address on the appropriate subnet. The product instructions were followed for applying the appropriate license keys to the virtual appliance, creating the default administrative user, as well as adding and configuring the four network interfaces.

Additionally, a separate VM was created for the purpose of forwarding exported session keys to the Redis server used by AppViewX and other decryptors. This server runs a syslog server, and converts messages containing keys to the FastKey JSON file, which are then pushed into Redis for use by the decryptors.


F5 BIG-IP Active Decryptor Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App1Interface_App1Network_App1IP_App1Purpose


The VM was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

Additional Modules
^^^^^^^^^^^^^^^^^^
The primary appliance was provisioned with the following modules from the ``System > Resource Provisioning`` menu item:

ENUMERATE_PluginName

F5 BIG-IP Syslog Server Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App2Interface_App2Network_App2IP_App2Purpose

This VM, running Ubuntu 20.04.6 LTS was created with a resource allocation including 8 vCPUs, 16 GB of memory, and 75 GB of storage.

.. include:: AppendixBGeneration/f5syslog.rst
