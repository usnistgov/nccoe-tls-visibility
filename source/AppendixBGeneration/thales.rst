Protecting Key Material in AppViewX Using the Thales HSM
=============================

This section contains the configuration instructions for using the Thales TCT Luna HSM to ensure the secure storage of key material within the AppViewX key governance platform.

Instantiation of the Thales TCT Luna HSM
----------------------------------------

The Luna HSM from Thales TCT is a physical hardware appliance that was installed in a server rack within the physical lab environment. The physical lab network infrastructure was bridged to the virtual lab network segment and both the physical and virtual networking infrastructure were configured to use the same VLAN tag. The HSM hardware appliance has a single network interface.

Thales TCT Luna HSM Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | HSMNET     | N/A                    | Provides connectivity to AppViewX.                                                                |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


1. SSH into the hardware appliance as the appliance administrator account to access the Luna shell

2. Elevate the shell session privileges:

   ``hsm login -password <HSM admin password>``

3. Create a named "partition" within the HSM to hold the AppViewX data, providing the partition name, a password for accessing the partition, and a "domain":

   ``par create -par <partition_name> -pas <partition_password> -domain <domain> -f``







Configuration Procedure
-----------------------

This section contains instructions for configuring the AppViewX key governance product to use a master encryption secret derived from the Thales HSM to secure its store of key material. To do this, understand that the AppViewX application appliance consists of a number of services running in a Kubernetes ecosystem running on a Linux host. Some of the instructions are to be performed at the Linux host shell and others are performed through the AppViewX web-based management console.

#. The Thales TCT Luna Client software must be installed on the AppViewX appliance (not the AppViewX SSM appliance). The client software was installed to the ``/home/appviewx/appviewx/hsm`` directory._x000D_
_x000D_
_x000D_
#. The AppViewX dependency configuration information was updated to include the HSM by editing the file: ``/home/appviewx/appviewx/appviewx_dependences/properties/hsm``_x000D_
   to ensure the line: ``export ChrystokiConfigurationPath=/appviewx/dependencies/hsm/``_x000D_
_x000D_
_x000D_
   exists and is not commented._x000D_
_x000D_
_x000D_
#. The AppViewX configuration information was updated to include the HSM. This is done by editing the configuration for the avx-common-config Kubernetes pod by issuing the command:_x000D_
_x000D_
_x000D_
   ``kubectl edit cm avx-common -n absecon``_x000D_
_x000D_
_x000D_
   In the resulting editor, add the following line:_x000D_
_x000D_
_x000D_
   ``export ChrystokiConfigurationPath=/appviewx/dependencies/hsm/``_x000D_
_x000D_
_x000D_
   and then instruct Kubernetes to restart the avx-common-hsm pod._x000D_
_x000D_
_x000D_
#. With the necessary software dependencies installed and registered, the AppViewX application was configured to use the HSM using the web-based management console._x000D_
_x000D_
_x000D_
#. Navigate to ``Inventory > Device > HSM``.

   .. figure:: /images/figures/
      :width: 90%
      :alt: Image showing the HSM tab in AppViewX.

      AppViewX HSM Inventory





#. On the left-hand side of the screen, select the icon for ``Gemalto a Thales Company``._x000D_
_x000D_
_x000D_
#. Next click the plus sign icon in the top right of the screen to create a new HSM device entry._x000D_
_x000D_
_x000D_
#. In the resulting screen, choose deployment type ``General Purpose Network``._x000D_
_x000D_
_x000D_
#. Enter a name for the HSM device._x000D_
_x000D_
_x000D_
#. Choose ``Both`` for ``Implementation Type``._x000D_
_x000D_
_x000D_
#. Choose the ``Datacenter``, defaulting to absecon for the appliance._x000D_
_x000D_
_x000D_
#. Choose the ``HSM Slot`` to use._x000D_
_x000D_
_x000D_
#. Enter the partition password as configured earlier._x000D_
_x000D_
_x000D_
#. Choose a ``Key Handler Name`` of appviewx-all.

   .. figure:: /images/figures/
      :width: 90%
      :alt: Image showing the configuration parameters for the HSM device.

      AppViewX HSM Configuration Parameters








Additional Configuration Files
------------------------------

+-----------------------------------------------------------------+
| Relevant Configuration Files                                    |
+=================================================================+

[[Configuration Files Description]]

