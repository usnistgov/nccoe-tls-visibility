.. _netscout:

NETSCOUT for Visibility Analytics
=============================

This section contains detailed instructions configuring the NetScout products used to perform real-time and post facto traffic analytics. These analytic capabilities are leveraged across all the real-time and post facto decryption previously described approaches. 

Instantiation of the NETSCOUT Virtual Appliances
------------------------------------------------

The NETSCOUT platform consists of four virtual appliances created from the vendor supplied OVF files: a vSTREAM appliance, vCYBERSTREAM appliance, nGeniusONE appliance, and an Omnis Cyber Intelligence (OCI) appliance. The vSTREAM and vCYBERSTREAM appliances are provisioned with three network interfaces, and the nGeniusOne and OCI appliances are each configured with a single network interface. 

The vSTREAM appliance improves visibility into virtualized and cloud environments with deep packet inspection to further performance management and security. It is used in this build to provide decrypted and encrypted traffic to the NETSCOUT nGeniusONE appliance.

The vCYBERSTREAM appliance assists in detection, investigation, and response to cyberthreats in real-time by leveraging packet-level data to identify suspicious activity across virtualized and cloud environments.

NetScout vSTREAM Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | MANAGEMENT | 192.168.10.4           | Connectivity to ISNG appliance.                                                                   |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 2         | ENCRYPTED  | N/A Layer 2 connection | Access to the encrypted network data provided by the network tap.                                 |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 3         | DECRYPTED  | N/A Layer 2 connection | Access to the network where decryptors output the decrypted traffic.                              |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


NetScout vCYBERSTREAM Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                                                           |
+===========+============+========================+===================================================================================================+
| 1         | MANAGEMENT | 192.168.10.4           | Connectivity to ISNG appliance.                                                                   |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 2         | ENCRYPTED  | N/A Layer 2 connection | Access to the encrypted network data provided by the network tap.                                 |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+
| 3         | DECRYPTED  | N/A Layer 2 connection | Access to the network where decryptors output the decrypted traffic.                              |
+-----------+------------+------------------------+---------------------------------------------------------------------------------------------------+


NetScout nGeniusOne Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+------------------------+----------------------------------------------------------------------+
| Interface | Network    | IP Address             | Purpose                                                              |
+===========+============+========================+======================================================================+
| 1         | MANAGEMENT | 192.168.10.4           | Connectivity to OCI appliance                                        |
+-----------+------------+------------------------+----------------------------------------------------------------------+


NetScout OCI Virtual Appliance Network Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------+
| Interface | Network    | IP Address     | Purpose                                                                        |
+===========+============+================+================================================================================+
| 1         | MANAGEMENT | 192.168.10.3   | Access to the web-based management console and connectivity to other products. |
+-----------+------------+----------------+--------------------------------------------------------------------------------+


Real-time Analytics
-------------------
The passive real-time decryptors and the break and inspect middleboxes each forward decrypted TLSv1.3 traffic to the real-time analytics platform over an isolated and secured network channel labeled ``DECRYPTED``. The real-time analytics are then performed on these streams of decrypted traffic within a limited time of the decrypted traffic's receipt. The decrypted traffic is retained by the analytics platform only as necessary and only for a short period of time.

The decrypted traffic can be analyzed from the NetScout OCI user interface, by navigating to the ``Security Events Center``. From here, you can search for events in a given time period - these events will be generated by suricata internally.

.. figure:: /images/figures/netscout-security-events-center.png
   :width: 90%
   :alt: Image showing the Security Events Center.

   Security Events Center in NetScout OCI

Post-Facto Analytics
--------------------

In each of the lab builds, encrypted traffic is intercepted and forwarded to the post facto analytics platform by a network tap on the ``SERVER`` network segment over the ``ENCRYPTED`` network segment. The post facto analytics platform is responsible for securely managing the captured traffic, including its eventual destruction. Real world implementations of these architectures would require network taps from all of the various physical and logical networks that make up the data center's logical data plane. For the middlebox builds, an additional network tap may be placed on the client-facing network segment. Alternatively, the middlebox may copy the incoming and outgoing encrypted traffic directly to the ``ENCRYPTED`` network.

The traffic decrypted by NetScout can be viewed by navigating to ``Packet Analysis`` on the nGeniusOne appliance.
From here, select an interface, and time period (or ``Live Capture``). Check the box next to ``SSL Decode`` to instruct NetScout to decrypt the traffic, and click ``Decode``. 

.. figure:: /images/figures/netscout-packet-analysis.png
   :width: 90%
   :alt: Image showing the Packet Analysis module.
   
   Packet Analysis in NetScout nGeniusOne





Configuration Procedure
-----------------------

The NetScout product was configured to receive traffic from the ``DECRYPTED`` and ``ENCRYPTED`` interfaces, such that it would perform in both the post-facto and real-time scenarios. Additional configuration to fine-tune the IDS to support the demonstration scenarios detailed in Appendix F, and demonstrate the visibility of the contents of the ``DECRYPTED`` traffic stream and the ability to decrypt the ``ENCRYPTED`` traffic stream using keys from the Diffie Hellman and Exported Session Keys scenarios.




The figure below shows how to add HTTPS traffic known to be decrypted as an application under HTTP in NetScout's application configuration. This will instruct NetScout to interpret that traffic as decrypted.

.. figure:: /images/figures/netscout-application-settings.png
   :width: 90%
   :alt: Image showing the addition of an application in NetScout Application Configuration to show HTTPS traffic as HTTP.

   Application Configuration allowing HTTPS to be viewed as HTTP.









Additional Configuration Files
------------------------------

+-----------------------------------------------------------------+
| Relevant Configuration Files                                    |
+=================================================================+
| vcyberstream/etc/suricata/suricata.yaml                         |
+-----------------------------------------------------------------+
| vcyberstream/custom-suricata-rules/suricata-rules.txt           |
+-----------------------------------------------------------------+

* ``custom-rules.txt`` contains the custom rules added to enable detection of the demonstration scenarios detailed in Appendix F. They are quite specific to these use cases to demonstrate feasibility and it is recommended to instead use open-source or more developed rulesets in practice.

* ``suricata.yaml`` contains a modified suricata.yaml used in this build. In particular some changes were made to enable the detection of SMTP messages, as well as for capturing files sent over TLS. Note that this file should be carefully reviewed and modified to meet the needs of an organization's systems, as some of the configurations used in development may add to latency or storage requirements.

