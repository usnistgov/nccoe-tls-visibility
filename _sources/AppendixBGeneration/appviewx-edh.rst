.. _appviewx-edh:

AppViewX for Bounded-Lifetime Server Key Governance
=============================

This build uses the AppViewX product to manage the creation, deployment, and retrieval of the bounded-lifetime ephemeral Diffie-Hellman keys used by the managed TLS servers to negotiate TLSv1.3 connections. A single implementation of the AppViewX platform is shared across all three of the builds.

Instantiation of the AppViewX Virtual Appliances
------------------------------------------------

To support this use case, two AppViewX products are deployed as virtual appliance machines. The main appviewX virtual appliance was created in vSphere from the vendor-supplied virtual appliance (OVF) file. It is provisioned with 8 vCPUs, 32 GB of memory, 250 GB of storage, and two network interfaces. This appliance is leveraged by the other use cases discussed later in the document.

The second virtual appliance, the Software Security Module, was created in vSphere from a separate OVF file supplied by the vendor. It is provisioned with 1 vCPU, 2 GB of memory, 40 GB of storage, and a single network interface. This appliance is only used for the generation, storage, distribution, and retrieval of the bounded-lifetime Diffie-Hellman key pairs that are used by the TLS servers.


AppViewX Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | MANAGEMENT | 192.168.10.15          | Access to the web-based management console and connectivity to other products.                    |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 2         | HSMNET     | N/A                    | Provides connectivity to the hardware security module.                                            |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


AppViewX Software Security Module Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+----------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                              |
+===========+============+========================+======================================================================+
| 1         | MANAGEMENT | 192.168.10.109         | Connectivity to other products.                                      |
+-----------+------------+------------------------+----------------------------------------------------------------------+


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

This section describes the configuration of AppViewX to do several things: periodically generate EDH keys, register the keys in the AppViewX Secure Software Module in a location available via SSH. The consumers of these keys include the decryptors and the TLSv1.3 configured servers which use them to form connections. In the case of these configured servers, the local NFR agent will pull the keys via SSH and make them available to the TLS application. Configuring AppViewX to manage the rotation and distribution of bounded-lifetime EDH keys is accomplished by installing two custom workflows through the AppViewX web console.

The figure below shows how to access the workflow library.

.. figure:: /images/figures/appviewx-workflows.png
   :width: 90%
   :alt: Image showing how to access the workflow library.

   Access to AppViewX Workflows





The figure below shows shows the contents of the workflow for the Diffie-Hellman workflow.

.. figure:: /images/figures/edh-workflow.png
   :width: 90%
   :alt: Image showing the contents of the Diffie Hellman workflow.

   Diffie-Hellman Key Rotation Workflow








Additional Configuration Files
------------------------------

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Relevant Configuration Files                                                                                                                                                                                          |
+=======================================================================================================================================================================================================================+
| `workflows/TLS 1_3 DH 2024/1st Attempt Key.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/1st%20Attempt%20Key.py>`__                              |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/Defining Curves.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/Defining%20Curves.py>`__                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/Encrypting and Archiving.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/Encrypting%20and%20Archiving.py>`__            |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/Executing Commands.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/Executing%20Commands.py>`__                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/Key Generation In.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/Key%20Generation%20In.py>`__                          |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/add_external_key.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/add_external_key.py>`__                                |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `workflows/TLS 1_3 DH 2024/final.py <https://github.com/usnistgov/nccoe-tls-visibility/blob/main/lab_build/appviewx/workflows/TLS%201_3%20DH%202024/final.py>`__                                                      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

These files were created  as part of the creation of the workflow for this build in AppViewX. This workflow serves the purpose of creating and registering keys with the AppViewX Secure Software module to make those keys available to the servers and decryptors which need them.

