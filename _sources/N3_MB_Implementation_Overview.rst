.. _E.4:

E.4 Architecture Implementation: Active Inspection Using Middleboxes
********************************************************************

Active inspection using middleboxes was implemented at both the OSI link layer (Layer 2) and the OSI network layer (Layer 3). 
Within the lab, only one middlebox implementation can be functional at any one time.  To demonstrate the Layer 2 configuration, the MIRA ETO Middlebox (``W``) was powered up and
the Layer 3 middlebox was powered down. Similarly, to demonstrate the Layer 3 configuration, the F5 Middlebox (``T``) was
powered up and the Layer 2 middlebox was powered down.

.. _Figure_Detailed_Arch:

.. figure:: /images/figures/Figure-1-4-v2.png
   :width: 90%
   :alt: Image showing the detailed architecture.

   Architecture and Networking details.


In order to route traffic appropriately in either configuration, the middleboxes were wired in tandem between the Data Center Border Router (``RA``) and the Data Center Segment Router (``RB``).  :ref:`Figure_E-1`, below,
shows the wiring configurations between the two routers and two middleboxes. 

.. _Figure_E-1:

.. figure:: /images/figures/Figure-1-5-v1.png
   :width: 90%
   :alt: Image showing split path between middlebox networking, allowing for the option to switch between Layer 2 and Layer 3 middlebox implementations in the same build.

   Middlebox Networking Details


.. _E.4.1:

E.4.1 Layer 2 Networking Configuration
======================================


The Layer 2 middlebox is invisible to routers ``RA`` and ``RB``.  When it is powered up, ARP requests from ``RA`` and ``RB`` are copied between ``SRVPATCHB1`` and ``SRVPATCHB2`` such that ``RA`` and ``RB`` have direct connections on the ``192.168.80.0/24`` network.  
The use of three separate subnets between the middleboxes and the routers ensures that regardless of which combination is active, there is a path to the ``SERVER`` network segment.

.. _E.4.2:

E.4.2 Layer 3 Networking Configuration
======================================

* ``SRVPATCHA1`` is assigned to the ``192.168.60.0/24`` network space.
* ``SRVPATCHA2`` is assigned to the ``192.168.70.0/24`` network space.


When the Layer 3 middlebox is powered up, router ``RA`` establishes a TCP connection to the middlebox ``T`` over network segment ``SRVPATCHA1``.

All traffic destined for a TLS server on the ``SERVER`` network has its IP address re-written from the ``192.168.30.0/24`` address space, to an address in the ``192.168.60.0/24`` space by the router ``RA``, using the same final octet value in both address spaces.
The F5 middlebox is then configured as a proxy that listens for connections to ``192.168.60.0/24``.  
When a connection to ``192.168.60.0/24`` is received, the middlebox establishes a connection to the TLS server with the equivalent ``192.168.30.0/24`` address.  
The middlebox has connectivity to the ``SERVER`` network segment through network segment ``SRVPATCHA2`` and router ``RB``. 



.. include:: N3_MB_Implementation_OSI2.rst

.. include:: N3_MB_Implementation_OSI3.rst

