.. _scenario-3.1a:

Scenario 3.1a: Malicious HTTPS File Serving
===========================================

Purpose
-------

Scan network traffic for instances of malicious files being transmitted over HTTPS.

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on potential malware being communicated over the network. A traffic generation script will be used to relay payloads over HTTPS to demonstrate this capability.

Procedure
---------

1. Use script3.1a to make a request to a webserver configured to serve a malicious file.
2. Observe the detection of the malicious file's hash in NetScout's Security Events Center.

Expected Outcome
----------------

The malicious file served over HTTP is detected as malicious by NetScout's internal IDS.

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



.. figure:: /images/demonstration_results/3.1a.http-malware.png
   :width: 90%
   :alt: A screenshot of NetScout's OCI interface showing the detection of a malicious file sent over HTTPS.

   Detection of malicious file being transmitted over decrypted HTTPS.




