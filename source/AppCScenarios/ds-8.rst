.. _scenario-3.1b:

Scenario 3.1b: Malicious SMTP Attachment
========================================

Purpose
-------

Scan network traffic for instances of malicious attachments in SMTP.

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on potential malware being communicated over the network. A traffic generation script will be used to relay payloads over SMTP to demonstrate this capability.

Procedure
---------

1. Use script3.1b to send a malicious file as an attachment from an external SMTP server to an internal SMTP server.
2. Observe the detection of the malicious file's hash in NetScout's Security Events Center.

Expected Outcome
----------------

The malicious file attachment sent over SMTP is detected as malicious by NetScout's internal IDS.

+-------------------------------------------------+-------------------------------------------------+
| Passive                                         | Active                                          |
+------------------------+------------------------+------------------------+------------------------+
| Bounded Life-Time      | Exported Session Key   | Break & Inspect (Mira) | Break and Inspect (F5) |
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+
| Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto | Real-Time | Post-Facto |
+===========+============+===========+============+===========+============+===========+============+
| Pass      | Pass       | Pass      | Pass       | Pass      | Pass       | N/A       | N/A        | 
+-----------+------------+-----------+------------+-----------+------------+-----------+------------+

Screenshots
-----------



.. figure:: /images/demonstration_results/3.1b.smtp-malware.png
   :width: 90%
   :alt: A screenshot of NetScout's OCI interface showing the detection of a malicious file sent over SMTP over TLS.

   Detection of malicious file being transmitted over SMTP over TLS.




