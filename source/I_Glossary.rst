.. _Glossary:

A. Glossary
^^^^^^^^^^^^^^^^^^^^

We use the terms from NISTIR 7298, *Glossary of Information Security
Terms* :ref:`[18]<nist_glossary>`__ or IETF RFC 4949, *Internet Security
Glossary*, Version 2 :ref:`[19]<ietf_terms>`__ where those references
define the terms.

+------------------+------------------------------------------------------+
| **Analytics**    | The discipline that applies logic and mathematics to |
|                  | data to provide insights for event recognition and   |
|                  | for making response decisions. In this project, the  |
|                  | function is executed by a set of tools for examining |
|                  | unencrypted payloads to identify undesired           |
|                  | characteristics.                                     |
+------------------+------------------------------------------------------+
| **Bounded        | A key variable that is used within the enterprise    |
| -Lifetime        | for decryption in real time or is stored for a       |
| Key**            | period established by an explicit enterprise policy  |
|                  | to enable decryption for post-facto security         |
|                  | analytics/forensics purposes and is then destroyed   |
|                  | in accordance with the policy.                       |
+------------------+------------------------------------------------------+
| **Break and      | A function that taps, decrypts, terminates, and      |
| Inspect**        | re-encrypts/reinitiates network traffic.             |
+------------------+------------------------------------------------------+
| **Certificate**  | A set of data that uniquely identifies a public key  |
|                  | (which has a corresponding private key) and an owner |
|                  | that is authorized to use the key pair. The          |
|                  | certificate contains the owner's public key and      |
|                  | possibly other information and is digitally signed   |
|                  | by a certificate authority (i.e., a trusted party),  |
|                  | thereby binding the public key to the owner.         |
+------------------+------------------------------------------------------+
| **Certificate    | An authorized entity that stores, signs, and issues  |
| Authority**      | digital cryptographic key certificates. It acts to   |
|                  | validate identities and bind them to cryptographic   |
|                  | key pairs with digital certificates.                 |
+------------------+------------------------------------------------------+
| **Certificate    | Functions for securely issuing, monitoring,          |
| and Key          | facilitating, and executing digital X.509            |
| Governance**     | certificates and managing the cryptographic keys     |
|                  | exchanged using the certificates.                    |
+------------------+------------------------------------------------------+
| **Client**       | System entities that request and use a service       |
|                  | provided by another system entity called a server.   |
|                  | Usually, it is understood that the client and server |
|                  | are automated components of the system, and the      |
|                  | client makes the request on behalf of a human user.  |
|                  | Clients may initiate encrypted traffic. They are     |
|                  | interfaces for human users, devices, applications,   |
|                  | and processes to access network functions, including |
|                  | the requesting of certificates and keys.             |
+------------------+------------------------------------------------------+
| **Cryptography** | The discipline that embodies the principles, means,  |
|                  | and methods for the transformation of data to hide   |
|                  | their semantic content, prevent their unauthorized   |
|                  | use, or prevent their undetected modification. It    |
|                  | embodies the principles, means, and methods for      |
|                  | providing information security, including            |
|                  | confidentiality, data integrity, non-repudiation,    |
|                  | and authenticity.                                    |
+------------------+------------------------------------------------------+
|                  | The process of a confidentiality mode that           |
| **Decryption**   | transforms encrypted data into the original usable   |
|                  | data.                                                |
+------------------+------------------------------------------------------+
| **Deep Packet    | A form of packet filtering that locates, identifies, |
| Inspection**     | classifies, and reroutes or blocks packets with      |
|                  | specific data or code payloads that conventional     |
|                  | packet filtering, which examines only packet         |
|                  | headers, cannot detect.                              |
+------------------+------------------------------------------------------+
| **DevOps**       | A combination of the terms development and           |
|                  | operations; meant to represent a collaborative or    |
|                  | shared approach to the tasks performed by a          |
|                  | company's application development and IT operations  |
|                  | teams.                                               |
+------------------+------------------------------------------------------+
| **Diffie         | A method used to securely exchange or establish      |
| -Hellman**       | secret keys across an insecure network. Ephemeral    |
|                  | Diffie-Hellman is used to create temporary or        |
|                  | single-use secret keys.                              |
+------------------+------------------------------------------------------+
| **Encryption**   | Cryptographic transformation of data (called         |
|                  | "plaintext") into a form (called "ciphertext") that  |
|                  | conceals the data's original meaning to prevent it   |
|                  | from being known or used. If the transformation is   |
|                  | reversible, the corresponding reversal process is    |
|                  | called "decryption," which is a transformation that  |
|                  | restores encrypted data to its original state.       |
+------------------+------------------------------------------------------+
| **Endpoint       | A lightweight background application installed on a  |
| Agent**          | device's operating system to constantly assess it    |
|                  | for vulnerabilities.                                 |
+------------------+------------------------------------------------------+
| **Ephemeral      | A cryptographic key that is generated for each       |
| Key**            | execution of a key-establishment process and that    |
|                  | meets other requirements of the key type (e.g.,      |
|                  | unique to each message or session).                  |
+------------------+------------------------------------------------------+
| **Key**          | A numerical value used to control cryptographic      |
|                  | operations, such as decryption, encryption,          |
|                  | signature generation, or signature verification.     |
|                  | Usually, a sequence of random or pseudorandom bits   |
|                  | used initially to set up and periodically change the |
|                  | operations performed in cryptographic operations for |
|                  | the purpose of encrypting or decrypting electronic   |
|                  | signals, or for producing another key.               |
+------------------+------------------------------------------------------+
| **Key            | Captures of session keys at the time they are        |
| Capture**        | negotiated.                                          |
+------------------+------------------------------------------------------+
| **Key            | The handling of cryptographic keys and other related |
| Management**     | security parameters (e.g., passwords) during the     |
|                  | entire life cycle of the keys, including their       |
|                  | generation, storage, establishment, entry and        |
|                  | output, and destruction.                             |
+------------------+------------------------------------------------------+
| **Key            | A function in the lifecycle of a cryptographic key;  |
| Registration**   | the process of a registration authority officially   |
|                  | recording the keying material.                       |
+------------------+------------------------------------------------------+
| **Key            | A FIPS 140-validated entity that securely generates  |
| Source**         | cryptographic keys and key pairs that are used in    |
|                  | cryptography.                                        |
+------------------+------------------------------------------------------+
| **Kubernetes**   | A portable, extensible, open-source platform for     |
|                  | managing containerized workloads and services, that  |
|                  | facilitates both declarative configuration and       |
|                  | automation.                                          |
+------------------+------------------------------------------------------+
| **Middlebox**    | A networking device that transforms, inspects,       |
|                  | filters, and manipulates traffic for purposes other  |
|                  | than packet forwarding. In this project, the device  |
|                  | is used to break and inspect enterprise network      |
|                  | traffic.                                             |
+------------------+------------------------------------------------------+
| **Network        | A component that provides a copy of traffic from a   |
| Tap**            | network segment. It is typically used in network     |
|                  | security applications to monitor traffic and         |
|                  | identify malicious activity or security threats.     |
+------------------+------------------------------------------------------+
| **Post-Facto**   | From or by an after act, or thing done afterward; in |
|                  | consequence of a subsequent act; retrospective.      |
+------------------+------------------------------------------------------+
| **Private        | The secret part of an asymmetric key pair that is    |
| Key**            | typically used to digitally sign or decrypt data.    |
+------------------+------------------------------------------------------+
| **Public         | The public part of an asymmetric key pair that is    |
| Key**            | typically used to verify signatures or encrypt data. |
+------------------+------------------------------------------------------+
| **Public Key     | A digital document issued and digitally signed by    |
| Certificate**    | the private key of a certificate authority that      |
|                  | binds an identifier to a cardholder through a public |
|                  | key. The certificate indicates that the cardholder   |
|                  | identified in the certificate has sole control and   |
|                  | access to the private key.                           |
+------------------+------------------------------------------------------+
| **Public Key     | A framework that is established to issue, maintain,  |
| Infrastructure** | and revoke public key certificates.                  |
|                  |                                                      |
+------------------+------------------------------------------------------+
| **QUIC**         | A UDP-based multiplexed and secure transport         |
|                  | `protocol                                            |
|                  |  <https://datatracker.ietf.org/doc/html/rfc9000>`__. |
+------------------+------------------------------------------------------+
| **Real-Time**    | A function which conducts operations that must       |
|                  | guarantee response times within a specified time or  |
|                  | window of time, usually relatively short.            |
+------------------+------------------------------------------------------+
| **SecOps**       | A combination of the terms security and operations;  |
|                  | a methodology that IT managers implement to enhance  |
|                  | the connection, collaboration, and communication     |
|                  | between IT security and IT operations teams.         |
+------------------+------------------------------------------------------+
| **Secret         | A cryptographic key that is used with a (symmetric)  |
| Key**            | cryptographic algorithm that is uniquely associated  |
|                  | with one or more entities and is not made public.    |
|                  | The use of the term "secret" in this context does    |
|                  | not imply a classification level, but rather implies |
|                  | the need to protect the key from disclosure.         |
+------------------+------------------------------------------------------+
| **Server**       | A system entity that provides services in response   |
|                  | to requests from other system entities called        |
|                  | clients.                                             |
+------------------+------------------------------------------------------+
| **Symmetric      | A cryptographic algorithm that uses the same secret  |
| Cryptography**   | key for its operation and, if applicable, for        |
|                  | reversing the effects of the operation (e.g., an AES |
|                  | key for encryption and decryption).                  |
+------------------+------------------------------------------------------+
| **Transport      | A security protocol providing privacy and data       |
| Layer            | integrity between two communicating applications.    |
| Security**       |                                                      |
+------------------+------------------------------------------------------+
| **TLS            | The counterparty for encrypted traffic that          |
| Server**         | generates session keys, negotiates encryption        |
|                  | protocols, and connects to key management            |
|                  | infrastructure.                                      |
+------------------+------------------------------------------------------+

