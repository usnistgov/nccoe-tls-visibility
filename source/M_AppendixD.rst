.. _AppendixD:

D. Description of the Example Architectures
####################################################
As indicated in :ref:`Architecture_and_Builds`, this appendix contains the detailed description of the three example architectures for achieving visibility of TLS 1.3 encrypted network traffic.

Return to :ref:`Architecture_and_Builds`.

.. _D.1:

D.1 Description of the Bounded-lifetime DH Key Architecture
***********************************************************

The figure below depicts the high-level architecture components and interactions that achieve visibility of TLSv1.3 traffic using rotated bounded-lifetime ephemeral Diffie-Hellman keys (EDH) on the TLS server. In this approach, the Key Governance Platform generates a new EDH key pair at a designated interval. The key pair is then simultaneously pushed to the TLS server and the real-time decryptor. The post facto analytics platform can query the Key Governance Platform using the TLS server name and connection time (epoch) of the session as parameters to retrieve the EDH server key for decrypting the stored TLS traffic stream. Additional details for this architecture are available in Section 5.2 of NIST SP 1800-37B: Approach, Architecture, and Security Characteristics.

.. figure:: /images/figures/Figure-1-1_v4.png
   :width: 90%
   :alt: Image showing Bounded-lifetime Diffie Hellman Key Architecture

   Bounded-lifetime Diffie Hellman Key Architecture

In the lab build for this reference architecture, software or services used for each of the architecture components can be found in the table below.

.. csv-table:: Build Components for the Passive Decryption Using Bounded-Lifetime EDH Keys Reference Architecture
   :widths: 20 15 40
   :header: "Architecture Component", "Collaborator", "Product Information"
   :file: csv/app_a_table3.csv

Return to :ref:`Middlebox Architecture<dh_arch>`.
Return to :ref:`Architecture and Builds<Architecture_and_Builds>`.


.. _D.2:

D.2 Description of the Exported Session Key Architecture
********************************************************

The figure below depicts the high-level architecture components and interactions that achieve visibility of TLSv1.3 traffic through the export of TLS session keys from the TLS server. In this approach, a Key Capture and Registration Agent installed on the TLS server retrieves the symmetric keys of each TLS session and forwards the key to the Real-time Decryptor which relays the key to the Key Governance Platform. The post facto analytics platform can retrieve the session keys by querying the Key Governance Platform using the client random identifier from the subject traffic stream. Additional details for this architecture are available in Section 5.2 of NIST SP 1800-37B: Approach, Architecture, and Security Characteristics. 

.. figure:: /images/figures/Figure-1-2_v4.png
   :width: 90%
   :alt: Image showing Reference Architecture for Passive Decryption Using Exported Session Keys

   Reference Architecture for Active Break and Inspect Decryption

In the lab build for this reference architecture, software or services used for each of the architecture components can be found in the table below.

.. csv-table:: Build Components for the Passive Decryption Using Exported Session Keys Reference Architecture
   :widths: 20 15 40
   :header: "Architecture Component", "Collaborator", "Product Information"
   :file: csv/app_a_table2.csv

Return to :ref:`Middlebox Architecture<ek_arch>`.
Return to :ref:`Architecture and Builds<Architecture_and_Builds>`.

.. _D.3:

D.3 Active Inspection Using a Break and Inspect Middlebox
*********************************************************

The figure below depicts the high-level architecture components and interactions that achieve visibility of TLSv1.3 traffic using active break and inspect middleboxes. In this approach, each TLS connection from a TLS client is terminated at the middlebox. The middlebox then initiates a second TLS connection to the target TLS server. The middlebox copies the TLS traffic from the client-facing TLS connection to the server-facing TLS connection while passing the clear text of the traffic to the Real-time Analytics Platform. Finally, the middlebox registers the ephemeral session key for each TLS session with the Key Governance Platform. The post facto analytics platform can retrieve the ephemeral keys by querying the Key Governance Platform using the client random identifier of the TLS session to be decrypted. Additional details for this architecture are available in Section 5.3 of NIST SP 1800-37B: Approach, Architecture, and Security Characteristics.

.. figure:: /images/figures/Figure-1-3_v4.png
   :width: 90%
   :alt: Image showing Reference Architecture for Active Break and Inspect Decryption

   Reference Architecture for Active Break and Inspect Decryption


The lab has two builds of this reference architecture: one that operates on traffic at the OSI Layer 3 level, and one that operates on the OSI Layer 2 level. In the lab build for the Layer 3 version of this reference architecture, the software or services used for each of the architecture components can be found in the tables below.


.. csv-table:: Build Components for the Active Inspection Using a Break and Inspect Middlebox Architecture (Layer 3 Implementation)
   :widths: 20 15 40
   :header: "Architecture Component", "Collaborator", "Product Information"
   :file: csv/app_a_table3.csv

.. csv-table:: Build Components for the Active Inspection Using a Break and Inspect Middlebox Architecture (Layer 2 Implementation)
   :widths: 20 15 40
   :header: "Architecture Component", "Collaborator", "Product Information"
   :file: csv/app_a_table4.csv

Return to :ref:`Middlebox Architecture<mb_arch>`.
Return to :ref:`Architecture and Builds<Architecture_and_Builds>`.



