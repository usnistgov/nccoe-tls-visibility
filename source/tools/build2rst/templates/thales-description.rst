Instantiation of the Thales TCT Luna HSM
----------------------------------------

The Luna HSM from Thales TCT is a physical hardware appliance that was installed in a server rack within the physical lab environment. The physical lab network infrastructure was bridged to the virtual lab network segment and both the physical and virtual networking infrastructure were configured to use the same VLAN tag. The HSM hardware appliance has a single network interface.

Thales TCT Luna HSM Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ENUMERATE_App1Interface_App1Network_App1IP_App1Purpose


1. SSH into the hardware appliance as the appliance administrator account to access the Luna shell

2. Elevate the shell session privileges:

   ``hsm login -password <HSM admin password>``

3. Create a named "partition" within the HSM to hold the AppViewX data, providing the partition name, a password for accessing the partition, and a "domain":

   ``par create -par <partition_name> -pas <partition_password> -domain <domain> -f``

