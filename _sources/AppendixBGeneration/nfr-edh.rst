.. _nfr-edh:

TLS Server Configuration with Not For Radio Using Bounded-Lifetime EDH Keys
=============================

This build uses the Not For Radio EVA product as the Key Management Agent on each TLS server. The build includes two HTTPS servers, a TLSv1.3-enabled instance of the MariaDB database server, and TLSv1.3-enabled instances of Postfix and Dovecot, for SMTP and IMAP connectivity, respectively. The following sections will provide the details of each of these servers, as well as the EVA agent configurations on each.

.. include:: AppendixBGeneration/rk-testapp.rst
.. include:: AppendixBGeneration/rk-mail.rst
.. include:: AppendixBGeneration/rk-keycloak.rst
.. include:: AppendixBGeneration/rk-mariadb.rst





Configuration Procedure
-----------------------

See configuration of individual TLS servers.




Additional Configuration Files
------------------------------

See configuration of individual TLS servers.

