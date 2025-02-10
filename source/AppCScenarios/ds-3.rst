.. _scenario-1.3:

Scenario 1.3: Error Code Logging (Layers)
=========================================

Purpose
-------

Identify, collect, and report on protocol-specific error status codes for services (Layer 4, 5, 6, and 7-type status codes).

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on layer-specific errors in an HTTP stack. A traffic generation script is used to produce error codes on various OSI layers in order to demonstrate the visibility of these errors at various levels.

Procedure
---------

1. Run script1.3 to generate errors on layers 4, 5, 6, and 7.
2. Observe the layer specific error codes in NetScout's Packet analysis tool.

Expected Outcome
----------------

The layer-specific error codes are visible in NetScout.

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



.. figure:: /images/demonstration_results/1.3.layer4.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted HTTP traffic during a Layer 4 error.

   Layer 4 (TLS) error code in a decrypted HTTP request.



.. figure:: /images/demonstration_results/1.3.layer5.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted HTTP traffic during a Layer 5 error.

   Layer 5 (Malformed Cookie) error code in a decrypted HTTP request.



.. figure:: /images/demonstration_results/1.3.layer6.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted HTTP traffic during a Layer 6 error.

   Layer 6 (Encoding) error code in a decrypted HTTP request.



.. figure:: /images/demonstration_results/1.3.layer7.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing decrypted HTTP traffic during a Layer 7 error.

   Layer 7 (404) error code in a decrypted HTTP request.




