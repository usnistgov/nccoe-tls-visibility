.. _scenario-1.2:

Scenario 1.2: Service Utilization
=================================

Purpose
-------

Identify and log protocol-specific distinct characteristics of Layer 5, 6, and 7-type service utilization and consumption information.

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on layer-specific information in an HTTP stack. A web request made through the browser is used to produce HTTPS traffic in order to demonstrate the visibility of the connection information at various levels.

Procedure
---------

1. Use a browser to navigate to the URL of the testapp server.
2. Observe the layer-specific decrypted traffic in NetScout's Packet Analysis tool.

Expected Outcome
----------------

The decrypted traffic is visible in NetScout and the layer-specific information is present.

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



.. figure:: /images/demonstration_results/1.2.normal-http.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted HTTP traffic.

   Layer specific information in a decrypted HTTP request.


.. figure:: /images/demonstration_results/1.2.web-services.png
   :width: 90%
   :alt: A screenshot of NetScout's Web Services interface showing statistics for decrypted HTTP traffic.

   Statistics for decrypted HTTP traffic.




