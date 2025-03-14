.. _nfr-ek:

Configuring TLS Servers with Not For Radio Using Exported Session Keys
=============================

This build uses the Not For Radio EVA product as the Key Management Agent on each TLS server. The build includes two HTTPS servers, a TLSv1.3-enabled instance of the MariaDB database server, and TLSv1.3-enabled instances of Postfix and Dovecot, for SMTP and IMAP connectivity, respectively. The following sections will provide the details of each of these servers, as well as the EVA agent configurations on each.

.. include:: AppendixBGeneration/ek-proxy.rst
.. include:: AppendixBGeneration/ek-testapp.rst
.. include:: AppendixBGeneration/ek-mail.rst
.. include:: AppendixBGeneration/ek-keycloak.rst
.. include:: AppendixBGeneration/ek-mariadb.rst





Configuration Procedure
-----------------------

See configuration of individual TLS servers.

Note that the integration for transferring exported session keys both to Mira and to the Redis server is enabled in the ``key_reporting`` section of ``eva.conf`` on each server.




Additional Configuration Files
------------------------------

See configuration of individual TLS servers.

