.. _AppendixB:

B. Descriptions of the Build implementations
#####################################################

The TLS 1.3 Visibility lab incorporates four implementations of the reference architectures within the same build environment:


* :ref:`B.2`,
* :ref:`B.3`,
* :ref:`B.4.1`, and
* :ref:`B.4.2`.


.. _B.1:

B.1 Shared Components Across All Builds
***************************************

.. include:: N0_Shared_Components.rst

.. _B.2:

B.2 Architecture Implementation: Passive Inspection Using Bounded-lifetime DH Keys
**********************************************************************************


.. include:: N1_RK_Implementation.rst


.. _B.3:

B.3 Architecture Implementation: Passive Inspection Using Exported Session Keys
*******************************************************************************

.. include:: N2_EK_Implementation.rst


.. _B.4:

B.4 Architecture Implementation: Active Inspection Using Middleboxes
********************************************************************

Active inspection using middleboxes was implemented at both the OSI link layer (Layer 2) and the OSI network layer (Layer 3). 
Within the lab, only one middlebox implementation can be functional at any one time.  To demonstrate the Layer 2 configuration, the MIRA ETO Middlebox (``W``) was powered up and
the Layer 3 middlebox was powered down. Similarly, to demonstrate the Layer 3 configuration, the F5 Middlebox (``T``) was
pwered up and the Layer 2 middlebox was powered down.

In order to route traffic appropriately in either configuration, the middleboxes were wired in tandem between the Data Center Border Router (``RA``) and the Data Center Segment Router (``RB``).  :ref:`Figure B-1`, below,
shows the wiring configurations between the two routers and two middleboxes. 

.. _Figure B-1:

Figure B-1: Middlebox Networking Details

.. image:: images/Middlebox_Network_Detail.svg

.. _B.4.1:

B.4.1 Layer 2 Networking Configuration
======================================


The Layer 2 middlebox is invisible to routers ``RA`` and ``RB``.  When it is powered up, ARP requests from ``RA`` and ``RB`` are copied between ``SRVPATCHB1`` and ``SRVPATCHB2`` such that ``RA`` and ``RB`` have direct connections on the ``192.168.80.0/24`` network.  
The use of three separate subnets between the middleboxes and the routers ensures that regardless of which combination is active, there is a path to the ``SERVER`` network segment.

.. _B.4.2:

B.4.2 Layer 3 Networking Configuration
======================================

* ``SRVPATCHA1`` is assigned to the ``192.168.60.0/24`` network space.
* ``SRVPATCHA2`` is assigned to the ``192.168.70.0/24`` network space.


When the Layer 3 middlebox is powered up, router ``RA`` establishes a TCP connection to the middlebox ``T`` over network segment ``SRVPATCHA1``.

All traffic destined for a TLS server on the ``SERVER`` network has its IP address re-written from the ``192.168.30.0/24`` address space, to an address in the ``192.168.60.0/24`` space by the router ``RA``, using the same final octet value in both address spaces.
The F5 middlebox is then configured as a proxy that listens for connections to ``192.168.60.0/24``.  
When a connection to ``192.168.60.0/24`` is received, the middlebox establishes a connection to the TLS server with the equivalent ``192.168.30.0/24`` address.  
The middlebox has connectivity to the ``SERVER`` network segment through network segment ``SRVPATCHA2`` and router ``RB``. 


.. _B.4.3:

B.4.3 Layer 2 Middlebox Implemention
====================================

.. include:: N3_MB_Implementation_OSI2.rst

.. _B.4.4:

B.4.4 Layer 3 Middlebox Implementation
======================================

.. include:: N3_MB_Implementation_OSI3.rst

