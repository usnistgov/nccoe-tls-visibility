.. _scenario-2.2:

Scenario 2.2: Proxy Error
=========================

Purpose
-------

Identify the propagation of performance issues throughout a system by correlating error status codes across component services.

Description
-----------

This demonstration shows how decrypted traffic can be utilized in tandem with a network proxy to provide visibility into network operations.

Procedure
---------

1. Use a browser to navigate to the URL of the testapp server behind a network proxy.
2. Observe the decrypted traffic in NetScout's Packet Analysis tool.

Expected Outcome
----------------

The decrypted traffic is visible in NetScout despite the use of a network proxy.

+-------------------------------------------------+-------------------------------------------------+
| Passive                                         | Active                                          |
+------------------------+------------------------+------------------------+------------------------+
| Bounded Life-Time      | Exported Session Key   | Break & Inspect (Mira) | Break and Inspect (F5) |
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+
| Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto |
+===========+============+===========+============+===========+============+===========+============+
| Pass      | Pass       | Pass      | Pass       | Pass      | Pass       | Pass      | Pass       | 
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+

Screenshots
-----------



.. figure:: /images/demonstration_results/2.2.http-over-proxy.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted traffic behind a proxy.

   Decrypted traffic behind a proxy.




