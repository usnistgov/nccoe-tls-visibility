AppViewX for Bounded-Lifetime Server Key Governance
=============================

This build uses the AppViewX product to manage the creation, deployment, and retrieval of the bounded-lifetime ephemeral Diffie-Hellman keys used by the managed TLS servers to negotiate TLSv1.3 connections. A single implementation of the AppViewX platform is shared across all three of the builds.

Instantiation of the AppViewX Virtual Appliances
------------------------------------------------

To support this use case, two AppViewX products are deployed as virtual appliance machines. The main appviewX virtual appliance was created in vSphere from the vendor-supplied virtual appliance (OVF) file. It is provisioned with 8 vCPUs, 32 GB of memory, 250 GB of storage, and two network interfaces configured as described in Table 2 5. This appliance is leveraged by the other use cases discussed later in the document.
The second virtual appliance, the Software Security Module, was created in vSphere from a separate OVF file supplied by the vendor. It is provisioned with 1 vCPU, 2 GB of memory, 40 GB of storage, and a single network interface configured as described in Table 2 6. This appliance is only used for the generation, storage, distribution, and retrieval of the bounded-lifetime Diffie-Hellman key pairs that are used by the TLS servers.


AppViewX Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+-----------------+--------------------------------------------------------------------------------+
| Interface | Network    | IP Address      | Purpose                                                                        |
+===========+============+=================+================================================================================+
| 1         | MANAGEMENT | 192.168.10.xxx  | Access to the web-based management console and connectivity to other products. |
+-----------+------------+-----------------+--------------------------------------------------------------------------------+
| 2         | HSMNET     | 192.168.yyy.xxx | Provides connectivity to the hardware security module                          |
+-----------+------------+-----------------+--------------------------------------------------------------------------------+


AppViewX Software Security Module Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------+
| Interface | Network    | IP Address     | Purpose                                    |
+===========+============+================+============================================+
| 1         | MANAGEMENT | 192.168.10.xxx | Access to the web-based management console |
+-----------+------------+----------------+--------------------------------------------+


Additional Modules
^^^^^^^^^^^^^^^^^^
The primary appliance was provisioned with the following modules:

+----------------------------------------------------------+--------------------------------------------------------------------------+
| Plugin Name                                              | Plugin Link                                                              |
+==========================================================+==========================================================================+
| AppViewX_2020.3.FP11.tar.gz                              | https://release.appviewx.com/downLoadArtifact?id=931                     |
+----------------------------------------------------------+--------------------------------------------------------------------------+
| scripts_2020.3.FP11_27Jul2023.tar.gz                     | https://release.appviewx.com/downLoadArtifact?id=1021                    |
+----------------------------------------------------------+--------------------------------------------------------------------------+
| appviewx_addons_2020.3.FP11.tar.gz                       | https://release.appviewx.com/downLoadArtifact?id=929                     |
+----------------------------------------------------------+--------------------------------------------------------------------------+
| AppViewX_2020.3.0_Latest_Plugins_01Sep2023_114616.tar.gz | https://release.appviewx.com/downLoadPluginAll?version=AppViewX_2020.3.0 |
+----------------------------------------------------------+--------------------------------------------------------------------------+
| N/A                                                      | https://release.appviewx.com/downLoadAddons?version=AppViewX_2020.3.0    |
+----------------------------------------------------------+--------------------------------------------------------------------------+







Configuration Procedure
-----------------------

SCREENSHOTS


Additional Configuration Files
------------------------------



[[Configuration Files Description]]

