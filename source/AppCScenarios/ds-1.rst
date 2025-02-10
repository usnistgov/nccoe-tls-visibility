.. _scenario-1.1:

Scenario 1.1: Expired TLS Certificates
======================================

Purpose
-------

Identify failed network traffic due to expired TLS PKI certificates (Layer 4).

Description
-----------

This demonstration shows how decrypted traffic can be used to report on expired TLS certificates and provide a path towards speedy remediation.

Procedure
---------

1. Assign an almost expired certificate to one of the proxy machines. 
2. Wait for the expiration date to elapse.
3. (MIRA) Observe the detection of the expired certificate in Mira's Session Log.
4. (F5) Observe the detection of the expired certificate in F5's Certificate Management.

Expected Outcome
----------------

The expiry of the certificate is visible in the user interface for the decryptor.

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



.. figure:: /images/demonstration_results/1.1.f5-expired.png
   :width: 90%
   :alt: A screenshot of F5's user interface which shows an expired certificate.

   F5 showing expired certificates in its list of certificates.



.. figure:: /images/demonstration_results/1.1.mira-expired.png
   :width: 90%
   :alt: A screenshot of Mira's user interface which shows an expired certificate in an active network flow.

   Mira showing expired certificates in the context of a network flow.



.. figure:: /images/demonstration_results/1.1.mira-reject.png
   :width: 90%
   :alt: A screenshot of Mira's user interface which shows a network flow being rejected because of it's certificate expiry.

   Mira rejecting traffic based on the expiry of the certificate.




