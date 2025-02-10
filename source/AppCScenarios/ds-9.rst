.. _scenario-3.2:

Scenario 3.2: Unexpected or Unauthorized Encryption 
====================================================

Purpose
-------

Identify network traffic that could not be decrypted.

Description
-----------

This demonstration shows how decrypted traffic can be utilized to identify, collect, and report on unauthorized or weakly encrypted connections on the network. A traffic generation script will be used to generate undesirable encrypted traffic.

Procedure
---------

1. Configure an HTTP server with a certificate that is not known to the decryption components. 
2. Observe the encrypted traffic in NetScout's Packet Analysis tool. Observe the identification of the traffic as unable to be decrypted in the active decryptor.

Expected Outcome
----------------

The decryptor identifies traffic it is unable to decrypt in the interface and the traffic shows as encrypted in NetScout.

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



.. figure:: /images/demonstration_results/3.2.still-encrypted.png
   :width: 90%
   :alt: A screenshot of NetScout's packet capture interface showing that the traffic is still decrypted.

   Traffic is not decrypted.



.. figure:: /images/demonstration_results/3.2.key-not-found.png
   :width: 90%
   :alt: A screenshot of Mira's user interface showing that the traffic has been separated as a separate flow, for which the key is not known.

   Undecryptable flows are noted.




