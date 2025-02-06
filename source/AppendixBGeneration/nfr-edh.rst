TLS Server Configuration with Not For Radio Using Bounded-Lifetime EDH Keys
=============================

This build uses the Not For Radio EVA product as the Key Management Agent on each TLS server. The build includes two HTTPS servers, a TLSv1.3-enabled instance of the MariaDB database server, and TLSv1.3-enabled instances of Postfix and Dovecot, for SMTP and IMAP connectivity, respectively. The following sections will provide the details of each of these servers, as well as the EVA agent configurations on each.

.. include:: rk-testapp.rst
.. include:: rk-mail.rst
.. include:: rk-keycloak.rst
.. include:: rk-mariadb.rst





Configuration Procedure
-----------------------

[[Configuration Procedure Summary]]




Additional Configuration Files
------------------------------

+-----------------------------------------------------------------+
| Relevant Configuration Files                                    |
+=================================================================+

[[Configuration Files Description]]

