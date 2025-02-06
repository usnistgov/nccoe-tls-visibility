Mail Server Configuration
-----------------------------

The Mail server build started with a standard Ubuntu 20.04.6 LTS virtual machine created with allocations of 2 vCPUs, 16 GB of memory, 50 GB of storage, and 2 network interface cards. 

Network Configuration
^^^^^^^^^^^^^^^^^^^^^

+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| Interface | Network    | Address        | Purpose                                                                                          |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 1         | MANAGEMENT | 192.168.30.15  | Management access to the server and transfer of session key material to Key Governance Platform. |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+
| 2         | SERVER     | 192.168.10.25  | Connectivity from TLS clients.                                                                   |
+-----------+------------+----------------+--------------------------------------------------------------------------------------------------+

Service Details
^^^^^^^^^^^^^^^
+-------------+-----------+---------------+
| Service     | Version   | Containerized |
+=============+===========+===============+
| Postfix     | 3.4.13    | No            |
+-------------+-----------+---------------+
| Dovecot     | 1:2.3.7.2 | No            |
+-------------+-----------+---------------+
| OpenSSL     | 1.1.1f    | No            |
+-------------+-----------+---------------+


Notes
^^^^^

The Mail application server consists of a Postfix service and Dovecot service providing SMTP and IMAP capabilities respectively.



The server was assigned the unique hostname rk-mail.visibility.nccoe.org. An associated "A" record for the server's hostname and IP address was recorded in the lab DNS service. The Mail software was installed using the native "apt" Ubuntu package installer.


First, a PKI certificate and key were created in PEM format using the DigiCert CertCentral service referencing the server's hostname. The certificate and key were uploaded to the VM and stored in the /home/tlsadmin/certs directory. Additionally, the DigiCert CertCentral CA certificate in PEM format was uploaded to the same folder.
Second, Mail was configured to only listen on the network interface connected to the SERVER network. 


Configuration Files
^^^^^^^^^^^^^^^^^^^

+--------------------------------------------------------------------------------+
| Configuration Files                                                            |
+================================================================================+
| /home/administrator/make-ssh-chroot.ssh                                        |
+--------------------------------------------------------------------------------+
| /etc/dovecot/dovecot.conf                                                      |
+--------------------------------------------------------------------------------+
| /etc/postfix/main.cf                                                           |
+--------------------------------------------------------------------------------+
| /etc/postfix/master.cf                                                         |
+--------------------------------------------------------------------------------+
| /etc/eva/eva-openssl.cnf                                                       |
+--------------------------------------------------------------------------------+
| /etc/eva/eva.conf                                                              |
+--------------------------------------------------------------------------------+

Postfix is configured to listen for incoming TLSv1.3 connections on the SERVER network. The Key Management Agent receives key material through an SSH connection from the Key Governance Platform over the MANAGEMENT network, authenticated using an SSH key pair. The Postfix server is secured with an SSL certificate issued through DigiCert. 

* ``eva-openssl.cnf`` contains config lines which are included in ``openssl.cnf``. It details which services should use the EVA agent to retrieve keys from AppViewX and use them in the workflow.
* ``eva.conf`` contains details on how to retrieve these keys.
* ``override.conf`` contains instructions for the system to ensure that the EVA agent is running prior to the affected service.

In addition to the configs listed, it was also necessary to create MX records in the DNS for each mail server present in the build, to ensure that the external mail server could communicate with them. In this case, the following was added to ``DNS Resolver > General Settings > Custom options ...`` in the PFSense firewall:

``local-data: "rk-mail.visibility.nccoe.org. IN MX 10 ek-mail.visibility.nccoe.org"``

Certificates location: ``/home/tlsadmin/certs``

Startup Instructions
^^^^^^^^^^^^^^^^^^^^

Finally, the Mail service was enabled through the following commands:

.. code-block:: bash

    # Note that by default these start automatically with system boot.

    service postfix start

    service dovecot start