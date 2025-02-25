Instantiation of the AppViewX Virtual Appliances
------------------------------------------------

To support this use case, two AppViewX products are deployed as virtual appliance machines. The main appviewX virtual appliance was created in vSphere from the vendor-supplied virtual appliance (OVF) file. It is provisioned with 8 vCPUs, 32 GB of memory, 250 GB of storage, and two network interfaces. This appliance is leveraged by the other use cases discussed later in the document.

The second virtual appliance, the Software Security Module, was created in vSphere from a separate OVF file supplied by the vendor. It is provisioned with 1 vCPU, 2 GB of memory, 40 GB of storage, and a single network interface. This appliance is only used for the generation, storage, distribution, and retrieval of the bounded-lifetime Diffie-Hellman key pairs that are used by the TLS servers.


AppViewX Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App1Interface_App1Network_App1IP_App1Purpose


AppViewX Software Security Module Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App2Interface_App2Network_App2IP_App2Purpose


Additional Modules
^^^^^^^^^^^^^^^^^^
The primary appliance was provisioned with the following modules:

ENUMERATE_PluginName_PluginLink


.. include:: AppendixBGeneration/redis.rst