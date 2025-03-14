.. _scenario-2.3:

Scenario 2.3: Bandwidth Utilization
===================================

Purpose
-------

Identify, collect, and report on network bandwidth utilization by service, sub-service, user, or client.

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on services using large amounts of bandwidth potentially for the purpose of degrading system response. An HTTP server was used in this demonstration and large amounts of traffic was sent to the endpoint using an invalid POST method.

Procedure
---------

1. Use script2.3 to generate a large amount of POST requests.
2. Observe the large amounts of POST requests in NetScout's Packet Analysis and NetScout OCI's Security Events Center.

Expected Outcome
----------------

The large number of packets is visible in NetScout.

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



.. figure:: /images/demonstration_results/2.3.bandwidth.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted POST requests and the frame count.

   POST requests decrypted frame count visible.


.. figure:: /images/demonstration_results/2.3.bandwidth-summary.png
   :width: 90%
   :alt: A screenshot of NetScout's Service Dashboard interface showing the number of transactions.

   Statistics showing number of transactions, sessions, and request failures.

.. figure:: /images/demonstration_results/2.3.bandwidth-traffic-monitor.png
   :width: 90%
   :alt: A screenshot of NetScout's Traffic Monitor interface showing statistics for traffic consuming the most bandwidth.

   Statistics comparing the bandwidth from various sources.



