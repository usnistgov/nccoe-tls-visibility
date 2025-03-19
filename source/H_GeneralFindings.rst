.. _General_Findings:
General Findings and Future Build Considerations
================================================

General Findings and Observations
---------------------------------

Each of the demonstrations identified in :ref:`Example Demonstration Events<demonstration_examples>` generated the
expected results. Specific details of the demonstration results are
provided in :ref:`Appendix F<AppendixF>`.

Future Build Considerations
---------------------------

Planning for Visibility with Post-Quantum Cryptography (PQC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Post-Quantum Cryptography (PQC) includes digital signature algorithms
and key encapsulation mechanisms (KEM)The TLS 1.4 visibility solutions
don't change key management, signature generation, or signature
verification processing. Therefore, the future use of PQC signature
algorithms will not impact the applicability of these visibility
solutions.

Likewise, TLS 1.3 visibility solutions that store session keys are not
impacted by the transition to PQC algorithms.

In the future, replacing the Diffie-Hellman algorithm with a PQC KEM
will have some impact on the visibility solutions. The figure below shows the
most likely use of a KEM in the TLS 1.3 handshake. Note: The only secret
key is held by the client. In the TLS 1.3 visibility solutions, the
servers are responsible for storing the short-lived Diffie-Hellman
private keys. However, this storage activity will fall to the client
when using short-lived PQC KEM secret keys. This is not a concern when
an enterprise employs a load balancer at the edge of the datacenter
since separate TLS 1.3 sessions are used on the public Internet and
inside the datacenter.


.. admonition:: Sample use of PQC KEM in TLS 1.3 Handshake

    **Client:**

    KEM. KeyGen() -> (pk, sk)

    Sent the public key (pk) to the server as part of the ClientHello

    **Server:**

    KEM.Encapsulate(pk) -> (ct, ss)

    Use the shared secret (ss) as an input to the key schedule

    Sent the ciphertext (ct) to the client in the ServerHello

    **Client:**

    KEM.Decapsulate(sk, ct) -> ss

    Use the shared secret (ss) as an input to the key schedule



Client-Based Monitoring
~~~~~~~~~~~~~~~~~~~~~~~

Client-based monitoring is an additional capability that is not within
the scope of the current demonstration project. It may be included in
future project extensions. The project examined server-focused options
rather than client-focused. Another approach to TLS 1.3 visibility
involves reliance on enterprise support directly by the client endpoint
or using clients via trusted proxy methods (e.g., SOCKS proxies). This
approach is reported to require no potential deviation from RFC 8446.
It also ensures that only those TLS clients mandated by local policy
(e.g., enterprise management, parental control, anti-malware protection
services) have these monitoring features available, and those only via
opt-in (directly or via their guardian).


